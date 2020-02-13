"""
A comparison of some functions that find the sum of every multiple of 3 or 5
below an upper bound. The code calls such a function a `FizzBuzzSummer`.

This was made because of an argument I had with my Dad on the code performance
of some hypothetical solutions to Project Euler's first problem.
Link: https://projecteuler.net/problem=1
"""

from argparse import ArgumentParser
from timeit import timeit
from typing import Callable, NamedTuple, Tuple


FizzBuzzSummer = Callable[[int], int]
class Solution(NamedTuple):
    name: str
    summer: FizzBuzzSummer


def summerA(n: int) -> int:
    """
    A naive solution. Iterates over every positive integer below the bound.
    """
    total = 0
    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            total += i
    return total

def summerB(n: int) -> int:
    """
    Iterates over the multiples only. Uses a set to avoid repeats.
    """
    total = 0
    fizzvisits = set()
    for i in range(0, n, 3):
        total += i
        fizzvisits.add(i)
    for j in range(0, n, 5):
        if j not in fizzvisits:
            total += j
    return total

def summerC(n: int) -> int:
    """
    Finds the sum of the union of the 3-multiples set and the 5-multiples set.
    My personal favorite solution, for the elegance. :3
    """
    return sum(set(range(0, n, 3)) | set(range(0, n, 5)))

def summerD(n: int) -> int:
    """
    Sums the 3-multiples with the 5-multiples, then subtracts the 15-multiples.
    """
    return sum(range(0, n, 3)) + sum(range(0, n, 5)) - sum(range(0, n, 15))

def summerE(n: int) -> int:
    """
    Uses the arithmetic series formula.
    Avoids generating the multiples, thanks to math.
    """
    def sum_multiples(divisor: int, terms: int) -> int:
        return divisor * (terms * (terms + 1)) // 2
    fizzsum      = sum_multiples( 3, (n-1) //  3)
    buzzsum      = sum_multiples( 5, (n-1) //  5)
    intersectsum = sum_multiples(15, (n-1) // 15)
    return fizzsum + buzzsum - intersectsum


def parse_args() -> Tuple[int, int]:
    """
    Gets the upper bound and number of trials arguments from the command line.
    """
    desc = (
        "Compare some functions that"
        " find the sum of every multiple of 3 or 5"
        " below an upper bound."
    )
    parser = ArgumentParser(description=desc)
    parser.add_argument("upperbound", type=int,
                        help="exclusive upper bound")
    parser.add_argument("trials", type=int,
                        nargs="?", default=1000,
                        help="numbers of timed trials")
    args = parser.parse_args()
    return args.upperbound, args.trials


def compare_solutions(bound: int, trials: int) -> None:
    """
    Prints out the solutions' outputs and execution times.
    """
    solutions = (
        Solution("Solution A", summerA),
        Solution("Solution B", summerB),
        Solution("Solution C", summerC),
        Solution("Solution D", summerD),
        Solution("Solution E", summerE)
    )

    print(f"Comparing solution outputs, using an upper bound of {bound}...")
    for sol in solutions:
        print(f"{sol.name}: {sol.summer(bound)}")

    print("")
    print(f"Comparing solution execution times using {trials} trials...")
    print(f"(Using the same upper bound of {bound}.)")
    for sol in solutions:
        print(f"{sol.name}: ", end="")
        print(timeit(lambda: sol.summer(bound), number=trials), end="")
        print(" seconds")


if __name__ == "__main__":
    compare_solutions(*parse_args())
