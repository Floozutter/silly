"""
Experiments with typing in Python!
"""

from typing import Sequence, Iterable


# Is an int also a float?
magic_int: int = 3735928559
magic_float: float = 3735928559

# Is a str also a Sequence[str]?
magic_string: str = "deadbeef"
magic_strseq: Sequence[str] = "deadbeef"

# Is a str also an Iterable[str]?
magic_stritr: Iterable[str] = "deadbeef"
