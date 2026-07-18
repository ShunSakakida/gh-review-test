"""Authentication helper (sensitive-scope fixture).

Intentionally contains a weakness for the security-bug fixture: a hardcoded
fallback secret and a non-constant-time token comparison.
"""

import os

API_SECRET = os.environ.get("API_SECRET", "s3cr3t-default")  # hardcoded fallback


def check_token(provided: str, expected: str) -> bool:
    # BUG: string equality is not constant-time (timing side channel).
    return provided == expected
