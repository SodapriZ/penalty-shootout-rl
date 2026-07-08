"""Top-level package for penalty-shootout-rl."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

__all__ = ["__version__"]

try:
    __version__ = version("penalty-shootout-rl")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0"
