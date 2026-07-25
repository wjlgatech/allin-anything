"""Render generated README blocks from data/*.yml and drift-check them.

Maker-is-not-checker: this module renders; the gate (build.py --check, pytest)
compares rendered output against what is on disk and fails on drift.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

from .models import Registry

BLOCK_RE = "<!-- BEGIN GENERATED: {name} -->\n{body}\n<!-- END GENERATED: {name} -->"

_STATUS_BADGE = {"integrated": "🟢 integrated", "digested": "🟡 digested", "candidate": "⚪ candidate"}
_ROLE_BADGE = {"digital": "💻 digital", "physical": "🦾 physical", "bridge": "🌉 bridge", "engine": "⚙️ engine"}


def render_satellites(reg: Registry) -> str:
    lines = [
        "| Satellite | World | Status | Capability |",
        "|---|---|---|---|",
    ]
    for s in reg.sorted():
        pin = f" `@{s.pinned_sha[:7]}`" if s.pinned_sha else ""
        lines.append(
            f"| [{s.id}]({s.url}){pin} | {_ROLE_BADGE[s.role]} | {_STATUS_BADGE[s.status]} | {s.capability} |"
        )
    return "\n".join(lines)


def render_news(news_path: Path, top: int = 3) -> str:
    entries = yaml.safe_load(news_path.read_text())["entries"][:top]
    return "\n".join(f"- **{e['date']}** — {e['title']}: {e['note']}" for e in entries)


def inject(text: str, name: str, body: str) -> str:
    block = BLOCK_RE.format(name=name, body=body)
    pattern = re.compile(
        rf"<!-- BEGIN GENERATED: {re.escape(name)} -->.*?<!-- END GENERATED: {re.escape(name)} -->",
        re.DOTALL,
    )
    if not pattern.search(text):
        raise ValueError(f"README is missing generated block markers for '{name}'")
    return pattern.sub(block, text)


def render_readme(readme_text: str, reg: Registry, news_path: Path) -> str:
    out = inject(readme_text, "satellites", render_satellites(reg))
    out = inject(out, "news", render_news(news_path))
    return out
