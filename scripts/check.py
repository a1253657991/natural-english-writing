#!/usr/bin/env python3
"""Check the skill package before committing: metadata, length, versions, pattern IDs, references, evals."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_SKILL_WORDS = 2200
MAX_DESCRIPTION_CHARS = 1024
errors = []


def fail(msg):
    errors.append(msg)


skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n(.*)$", skill, re.S)
if not m:
    sys.exit("SKILL.md: missing YAML frontmatter")
front, body = m.groups()

name = re.search(r"^name:\s*(\S+)", front, re.M)
if not name or name.group(1) != ROOT.name:
    fail(f"SKILL.md: name must equal the folder name '{ROOT.name}'")
desc = re.search(r"^description:\s*(.+)$", front, re.M)
if not desc:
    fail("SKILL.md: missing description")
elif len(desc.group(1)) > MAX_DESCRIPTION_CHARS:
    fail(f"SKILL.md: description is {len(desc.group(1))} chars (max {MAX_DESCRIPTION_CHARS})")
version = re.search(r'^\s+version:\s*"([\d.]+)"', front, re.M)
if not version:
    fail("SKILL.md: missing metadata.version")

words = len(body.split())
if words > MAX_SKILL_WORDS:
    fail(f"SKILL.md: body is {words} words (max {MAX_SKILL_WORDS})")

changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
first = re.search(r"^## ([\d.]+)", changelog, re.M)
if version and (not first or first.group(1) != version.group(1)):
    fail("CHANGELOG.md: first heading must match metadata.version")

for ref in sorted(set(re.findall(r"`(references/[\w.-]+)`", skill))):
    if not (ROOT / ref).is_file():
        fail(f"SKILL.md points to missing file {ref}")

patterns = (ROOT / "references" / "patterns.md").read_text(encoding="utf-8")
ids = re.findall(r"^(?:###|- \*\*)\s*([A-G])(\d+)\.", patterns, re.M)
by_group = {}
for group, num in ids:
    by_group.setdefault(group, []).append(int(num))
for group, nums in sorted(by_group.items()):
    if nums != list(range(1, len(nums) + 1)):
        fail(f"patterns.md: group {group} is numbered {nums}, expected 1..{len(nums)}")
contents = re.search(r"^Contents:(.*)$", patterns, re.M)
if contents:
    for group, last in re.findall(r"\(([A-G])1–[A-G](\d+)\)", contents.group(1)):
        if len(by_group.get(group, [])) != int(last):
            fail(f"patterns.md: Contents says {group}1–{group}{last}, found {len(by_group.get(group, []))}")

for case in sorted(p for p in (ROOT / "evals").iterdir() if p.is_dir() and p.name != "results"):
    for needed in ("prompt.md", "case.yaml"):
        if not (case / needed).is_file():
            fail(f"evals/{case.name}: missing {needed}")
    if not list((case / "graders").glob("*.md")):
        fail(f"evals/{case.name}: no graders")

total = sum(len(v) for v in by_group.values())
if errors:
    print("\n".join(f"FAIL {e}" for e in errors))
    sys.exit(1)
print(f"OK  version {version.group(1)}, SKILL.md {words} words, {total} patterns")
