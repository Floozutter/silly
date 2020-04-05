"""
Experiments with typing in Python!
"""

from typing import Sequence


# Is a str also a Sequence[str]?
magic_string: str = "deadbeef"
magic_strseq: Sequence[str] = "deadbeef"
