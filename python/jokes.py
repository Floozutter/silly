"""
Silly code that wasn't written to be ran.
"""

import random
import functools
from typing import AbstractSet, Mapping, Iterable, Any


# A random function, with a twist. (Read decorator last!)
@functools.lru_cache(maxsize=1)
def rand100() -> int:
    """Returns a random integer within [0, 100)."""
    return random.randrange(0, 100)

# Another memoized random function, but as a one-liner.
random.random = functools.lru_cache(maxsize=1)(random.random)


# SMH stands for SMH My Head.
def smh(depth: int = 0) -> str:
    """Expands smh as many times as the depth argument."""
    if depth == 0: return "smh"
    else:          return smh(depth-1) + " my head"


# A function that answers how you are.
def how_are_you(
    health: int,                             # Integer because health/points/.
    hunger: int,                             # Is high hunger good or bad?
    energy: int,                             # Boost using coffee.
    mental: int,                             # Mine's negative.
    status_ailments: AbstractSet[str],       # Stringly typed! >:O
    relationship_scores: Mapping[str, int],  # No "Player ID" type?
    current_thoughtstream: Iterable[str],    # I exhausted this.
    mood: Any,                               # Mood.
    is_actually_okay: bool = False           # :(
) -> str:
    """
    Returns an answer to the question "How are you?" using your current state.
    """
    return "Okay."




