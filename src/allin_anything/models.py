"""Typed models for the satellite registry (spec-as-data)."""

from __future__ import annotations

from dataclasses import dataclass, field

ROLES = ("digital", "physical", "bridge", "engine")
STATUSES = ("candidate", "digested", "integrated")
KINDS = ("external", "family")


@dataclass(frozen=True)
class Satellite:
    id: str
    kind: str
    role: str
    capability: str
    url: str
    status: str
    pinned_sha: str | None = None
    license: str | None = None
    visibility: str = "public"
    notes: str = ""

    @property
    def status_rank(self) -> int:
        return STATUSES.index(self.status) if self.status in STATUSES else -1


@dataclass(frozen=True)
class Registry:
    version: str
    updated: str
    satellites: tuple[Satellite, ...] = field(default_factory=tuple)

    def by_status(self, status: str) -> tuple[Satellite, ...]:
        return tuple(s for s in self.satellites if s.status == status)

    def sorted(self) -> tuple[Satellite, ...]:
        return tuple(
            sorted(self.satellites, key=lambda s: (-s.status_rank, s.id))
        )
