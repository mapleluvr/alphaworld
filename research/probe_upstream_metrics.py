"""Bounded counterexamples against the unchanged upstream measurement code.

These fixtures probe measurement semantics, not human/AI writing quality and not
reproduction of the private corpus. Run: python -B research/probe_upstream_metrics.py
"""
import importlib.util
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
UPSTREAM = ROOT / "lieflat-less-ai-tone"


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, UPSTREAM / "scripts" / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


structure = load_module("upstream_structure", "check-structure.py")
comparison = load_module("upstream_comparison", "compare-human-ai.py")

wrapped = "这个接口继续接受旧版请求。\n客户端无需修改现有参数。"
unwrapped = wrapped.replace("\n", "")
intro = "这个接口昨天完成了兼容性检查。\n\n"
with_reference = intro + "值得注意的是，这个接口仍然兼容旧版本。"
without_reference = intro + "值得注意的是，仍然兼容旧版本。"
headings = "## 一、核对接口约定\n## 二、运行兼容检查\n## 三、完成交付报告"
prose = "首先，核对接口约定。\n其次，运行兼容检查。\n最后，完成交付报告。"
heading_rule = "6 序数词当小标题"

report = {
    "upstream_commit": subprocess.check_output(
        ["git", "-C", str(UPSTREAM), "rev-parse", "HEAD"], text=True
    ).strip(),
    "scope": "Direct calls to unchanged upstream functions; synthetic measurement counterexamples only.",
    "paragraph_boundary": {
        "documented_unit": "blank-line-separated paragraphs",
        "wrapped_input": wrapped,
        "wrapped_paragraphs": structure.paragraphs(wrapped),
        "unwrapped_input": unwrapped,
        "unwrapped_paragraphs": structure.paragraphs(unwrapped),
    },
    "explicit_reference": {
        "documented_exemption": "Keep a comment sentence that already contains a reference such as 这.",
        "with_reference": {"input": with_reference, "measurement": structure.measure([with_reference])},
        "without_reference": {"input": without_reference, "measurement": structure.measure([without_reference])},
    },
    "heading_detection": {
        "documented_target": "Three or more numbered headings; ordinary prose 首先/其次 is exempt.",
        "headings": {"input": headings, "hits": comparison.measure([headings])[0][heading_rule][1]},
        "prose": {"input": prose, "hits": comparison.measure([prose])[0][heading_rule][1]},
    },
}

# Bind the recorded counterexamples to the observed upstream behavior.
assert len(report["paragraph_boundary"]["wrapped_paragraphs"]) == 2
assert len(report["paragraph_boundary"]["unwrapped_paragraphs"]) == 1
metric = "段首零主语评论/非首段%"
assert report["explicit_reference"]["with_reference"]["measurement"][metric] == 100
assert report["explicit_reference"]["without_reference"]["measurement"][metric] == 100
assert report["heading_detection"]["headings"]["hits"] == 0
assert report["heading_detection"]["prose"]["hits"] == 3

output = ROOT / "upstream-metric-probes.json"
output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(report, ensure_ascii=False, indent=2))
