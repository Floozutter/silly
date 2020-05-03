"""
A bodged solver for a puzzle from Aydin.

The puzzle is about finding and justifying a substitution for the "?":
    (A) 2, 4, 6, 6 -> 41
    (B) 3, 6, 7, 4 -> 52
    (C) 3, 7, 5, 5 -> ?
The options given for the substitution are 36, 48, 75, 50, and 47.
(Actually, the last option was "I don't know", but who'd pick that, lol.)
"""

import random
from itertools import count
from functools import reduce
from typing import Callable, Iterable, Tuple, NamedTuple


class Operation(NamedTuple):
    name: str
    function: Callable[[int, int], int]

OPERATIONS = (
    Operation("add",      lambda a, b: a + b),
    Operation("subtract", lambda a, b: a - b),
    Operation("multiply", lambda a, b: a * b),
    Operation("divide",   lambda a, b: a // b),
    Operation("concat",   lambda a, b: a*10 + b)
)


class Solution:
    argorder: Tuple[int, ...]
    operations: Tuple[Operation, ...]
    def __init__(self, argorder: Iterable[int], ops: Iterable[Operation]):
        self.argorder = tuple(argorder)
        self.operations = tuple(ops)
        assert len(self.operations) == len(self.argorder) - 1
    def function(self, args: Tuple[int, int, int, int]) -> int:
        orderedargs = (args[i] for i in self.argorder)
        first = next(orderedargs)
        return reduce(
            lambda val, opvalpair: opvalpair[0].function(val, opvalpair[1]),
            zip(self.operations, orderedargs),
            first
        )


def randSolution() -> Solution:
    """
    Randomly generates a Solution that uses all 4 arguments with 3 operations.
    """
    return Solution(
        random.sample(tuple(range(4)), k=4),
        random.choices(OPERATIONS, k=3)
    )


if __name__ == "__main__":
    A = (2, 4, 6, 6)
    B = (3, 6, 7, 4)
    C = (3, 7, 5, 5)
    A_result = 41
    B_result = 52

    print(f"{A} -> {A_result}")
    print(f"{B} -> {B_result}")
    print(f"{C} -> ?")
    print("Searching for a solution matching on A and B...")
    
    for i in count():
        sol = randSolution()
        if sol.function(A) == A_result and sol.function(B) == B_result:
            break

    print("")
    print(f"Argument Order by Index: {', '.join(map(str, sol.argorder))}")
    print(f"Operations: {', '.join(op.name for op in sol.operations)}")
    print(f"Solution on C: {sol.function(C)}")
