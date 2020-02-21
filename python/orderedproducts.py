"""
A comparison of some functions that generate the products of a multiplication
table in sorted order.

This always happens when I talk to Dad about a Project Euler problem, lol.
Link: https://projecteuler.net/problem=4
"""

from argparse import ArgumentParser
from timeit import timeit

from itertools import combinations_with_replacement
from heapq import merge
from collections import deque

from typing import Callable, NamedTuple, Tuple, Iterable, List


OrderedProducts = Callable[[int], Iterable[int]]
class Solution(NamedTuple):
    name: str
    op: OrderedProducts


def opA(upper: int) -> Iterable[int]:
    """
    Generates the products, then uses Python's built-in sort.
    """
    factors = range(1, upper)
    pairs = combinations_with_replacement(factors, 2)
    products = (p[0]*p[1] for p in pairs)
    return sorted(products)

def opB(upper: int) -> Iterable[int]:
    """
    Merges sorted rows of multiples for each factor, using heapq.
    """
    def multiples(factor: int) -> Iterable[int]:
        """
        Returns multiples of the factor in ascending order, up to factor^2.
        """
        return [factor*n for n in range(1, factor+1)]
    rows = (multiples(factor) for factor in range(1, upper))
    return merge(*rows)

def opC(upper: int) -> Iterable[int]:
    """
    Dad's thing...
    """
    for i in range(1, (upper-1)**2 + 1):
        for j in range(1, 2 + i // 2):
            quotient, remainder = divmod(i, j)
            if j < upper and quotient < upper and remainder == 0:
                yield i


def uniquelist(it: Iterable[int]) -> List[int]:
    """
    Returns a list of unique elements by removing duplicates from an Iterable.
    Preserves order.
    """
    return list(dict.fromkeys(it))

def exhaust(it: Iterable[int]) -> None:
    """
    Exhausts an Iterable.
    """
    deque(it, maxlen=0)


def parse_args() -> Tuple[int, int]:
    """
    Gets the upper bound and number of trials arguments from the command line.
    """
    desc = "Compare some functions that order the times table."
    parser = ArgumentParser(description=desc)
    parser.add_argument("upperbound", type=int,
                        help="exclusive upper bound")
    parser.add_argument("trials", type=int,
                        nargs="?", default=1,
                        help="numbers of timed trials")
    args = parser.parse_args()
    return args.upperbound, args.trials


def compare_solutions(upper: int, trials: int) -> None:
    """
    Prints out the solutions' outputs and execution times.
    """
    solutions = (
        Solution("Solution A", opA),
        Solution("Solution B", opB),
        Solution("Solution C", opC)
    )

    print(f"Comparing solution outputs, using an upper bound of {upper}...")
    print("(Outputs are compared as ordered lists of unique elements.)")
    benchmark = uniquelist(opA(upper))
    for sol in solutions:
        print(f"{sol.name}: ", end="")
        if uniquelist(sol.op(upper)) == benchmark:
            print("Matches benchmark!")
        else:
            print("Does NOT match benchmark!")

    print("")
    print(f"Comparing solution execution times using {trials} trials...")
    print(f"(Using the same upper bound of {upper}.)")
    for sol in solutions:
        print(f"{sol.name}: ", end="")
        print(timeit(lambda: exhaust(sol.op(upper)), number=trials), end="")
        print(" seconds")


if __name__ == "__main__":
    compare_solutions(*parse_args())
