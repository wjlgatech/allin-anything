"""Deterministic intent router over the satellite registry.

The flagship SKILL.md is the human-facing half; this is the executable half, so
routing claims are testable (every eval case is a pytest case, per the playbook).
"""

from __future__ import annotations

from .models import Registry, RouteDecision

_VENDOR_WORDS = ("copy", "vendor", "fork", "embed", "inline")


class Router:
    """Routes a natural-language intent to satellites using registry triggers.

    Precedence: refuse (license walls) > direct (satellite named verbatim) >
    trigger-scored route > none. Ties order by status rank, then match count.
    """

    def __init__(self, reg: Registry):
        self._reg = reg

    def route(self, intent: str) -> RouteDecision:
        """Return the verdict for one intent. Deterministic; no network, no model."""
        text = intent.lower()

        for s in self._reg.satellites:
            if s.kind == "external" and s.id in text and any(w in text for w in _VENDOR_WORDS):
                return RouteDecision(
                    mode="refuse",
                    satellite_ids=(s.id,),
                    reason=f"'{s.id}' is external ({s.license}); satellites are never vendored — run it upstream",
                )

        named = tuple(s.id for s in self._reg.satellites if s.id.lower() in text)
        if len(named) == 1:
            return RouteDecision(
                mode="direct",
                satellite_ids=named,
                reason=f"intent names '{named[0]}' — go direct, no routing needed",
            )

        scored = []
        for s in self._reg.satellites:
            hits = [t for t in s.triggers if t in text]
            if hits:
                scored.append((s.status_rank, len(hits), s))
        scored.sort(key=lambda x: (-x[0], -x[1], x[2].id))

        if not scored:
            return RouteDecision(mode="none", satellite_ids=(), reason="no satellite matched — bank the gap in data/news.yml")

        ids = tuple(s.id for _, _, s in scored)
        statuses = ", ".join(f"{s.id}={s.status}" for _, _, s in scored)
        return RouteDecision(mode="route", satellite_ids=ids, reason=f"trigger match ({statuses})")
