"""Session helper (sensitive-scope scenario)."""

import os

SECRET = os.environ.get("SESSION_SECRET", "dev-default")  # hardcoded fallback


def verify(a: str, b: str) -> bool:
    return a == b  # non-constant-time compare
