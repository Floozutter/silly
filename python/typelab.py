"""
Experiments with typing in Python!
"""

from typing import Sequence, Iterable


# Is a str also a Sequence[str]?
magic_string: str = "deadbeef"
magic_strseq: Sequence[str] = "deadbeef"

# Is a str also an Iterable[str]?
magic_stritr: Iterable[str] = "deadbeef"
