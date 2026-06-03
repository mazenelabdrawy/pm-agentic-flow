#!/usr/bin/env python3
"""
validate_agents.py — pre-submit validator for pm-flow contributions.

Checks, with no third-party dependencies:
  1. .claude-plugin/marketplace.json and plugin.json are valid JSON.
  2. eval/rubric.yaml parses (light structural check; full YAML if PyYAML present).
  3. Every skills/<name>/SKILL.md has frontmatter with `name` + `description`,
     and `name` matches its directory.
  4. Every SKILL.md contains the §7 agent-contract sections.
  5. Every PCO section a skill claims to read/write exists in docs/pco-schema.md.
  6. Every commands/*.md has frontmatter `description` (+ `argument-hint` recommended).

Exit code 0 = all good, 1 = problems found.

Usage:  python3 validate_agents.py
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
errors: list[str] = []
warnings: list[str] = []

# §7 contract sections every agent SKILL.md must contain.
REQUIRED_SECTIONS = ["## Role", "## Mode", "## Inputs", "## Outputs", "## Eval gate", "## System prompt"]


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def parse_frontmatter(text: str) -> dict | None:
    """Return a flat dict of top-level `key: value` pairs from a --- frontmatter block."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def load_pco_section_ids() -> set[str]:
    schema = ROOT / "docs" / "pco-schema.md"
    if not schema.exists():
        err("docs/pco-schema.md is missing — it is the spine; cannot validate PCO references.")
        return set()
    text = schema.read_text(encoding="utf-8")
    # The canonical ID list lives in the fenced block under "Section ID reference".
    block = re.search(r"Section ID reference.*?```(.*?)```", text, re.DOTALL)
    ids: set[str] = set()
    if block:
        for token in re.split(r"[·\n]", block.group(1)):
            t = token.strip()
            if t:
                ids.add(t)
    if not ids:
        err("Could not parse the PCO section ID list from docs/pco-schema.md.")
    return ids


def check_json(path: Path) -> None:
    if not path.exists():
        err(f"{path.relative_to(ROOT)} is missing.")
        return
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(f"{path.relative_to(ROOT)} is not valid JSON: {e}")


def check_rubric() -> None:
    path = ROOT / "eval" / "rubric.yaml"
    if not path.exists():
        err("eval/rubric.yaml is missing.")
        return
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore
        yaml.safe_load(text)
    except ImportError:
        if "gates:" not in text or "scoring_criteria:" not in text:
            warn("eval/rubric.yaml present but PyYAML not installed; basic check found "
                 "missing `gates:` or `scoring_criteria:` keys.")
    except Exception as e:  # noqa: BLE001
        err(f"eval/rubric.yaml does not parse as YAML: {e}")


def referenced_pco_ids(body: str) -> set[str]:
    """Pull the PCO section id from each Inputs/Outputs bullet.

    Convention: each bullet starts with the section id in backticks, e.g.
    `- ``synthesis``: key-insights, ...`. Only that leading token is a PCO
    *section*; later backticked tokens are sub-fields and are not validated here.
    """
    found: set[str] = set()
    for sec in ("## Inputs", "## Outputs"):
        m = re.search(re.escape(sec) + r".*?(?=\n## |\Z)", body, re.DOTALL)
        if not m:
            continue
        for line in m.group(0).splitlines():
            bullet = re.match(r"\s*-\s*`([a-z][a-z0-9-]+)`", line)
            if bullet:
                found.add(bullet.group(1))
    return found


def check_skills(pco_ids: set[str]) -> None:
    skills_dir = ROOT / "skills"
    if not skills_dir.exists():
        err("skills/ directory is missing.")
        return
    dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
    if not dirs:
        warn("No skills found yet.")
    for d in dirs:
        skill_md = d / "SKILL.md"
        if not skill_md.exists():
            err(f"skills/{d.name}/ has no SKILL.md.")
            continue
        text = skill_md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            err(f"skills/{d.name}/SKILL.md has no frontmatter block.")
            continue
        if not fm.get("name"):
            err(f"skills/{d.name}/SKILL.md frontmatter missing `name`.")
        elif fm["name"] != d.name:
            err(f"skills/{d.name}/SKILL.md `name: {fm['name']}` must match directory `{d.name}`.")
        if not fm.get("description"):
            err(f"skills/{d.name}/SKILL.md frontmatter missing `description`.")
        for sec in REQUIRED_SECTIONS:
            if sec not in text:
                err(f"skills/{d.name}/SKILL.md missing required section `{sec}`.")
        if pco_ids:
            for ref in referenced_pco_ids(text):
                if ref not in pco_ids:
                    err(f"skills/{d.name}/SKILL.md references unknown PCO section `{ref}` "
                        f"(add it to docs/pco-schema.md if intentional).")


def check_commands() -> None:
    cmd_dir = ROOT / "commands"
    if not cmd_dir.exists():
        err("commands/ directory is missing.")
        return
    cmds = sorted(cmd_dir.glob("*.md"))
    if not cmds:
        warn("No commands found yet.")
    for c in cmds:
        fm = parse_frontmatter(c.read_text(encoding="utf-8"))
        if fm is None:
            err(f"commands/{c.name} has no frontmatter block.")
            continue
        if not fm.get("description"):
            err(f"commands/{c.name} frontmatter missing `description`.")
        if not fm.get("argument-hint"):
            warn(f"commands/{c.name} frontmatter missing `argument-hint` (recommended).")


def main() -> int:
    check_json(ROOT / ".claude-plugin" / "marketplace.json")
    check_json(ROOT / ".claude-plugin" / "plugin.json")
    check_rubric()
    pco_ids = load_pco_section_ids()
    check_skills(pco_ids)
    check_commands()

    for w in warnings:
        print(f"  warn: {w}")
    if errors:
        print(f"\n✗ {len(errors)} problem(s) found:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"\n✓ pm-flow validation passed ({len(warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
