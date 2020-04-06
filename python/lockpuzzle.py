"""
A bodged solver for a puzzle involving a combination lock that Mikle sent me.

The puzzle is about finding a solution to a 3-digit combination lock.
The clues are given in relation to example combinations:
    682 - "One digit is right and in its place."
    614 - "One digit is right but in the wrong place."
    206 - "Two digits are right but both are in the wrong place."
    738 - "All digits are wrong."
    380 - "One digit is right but in the wrong place."
"""

from typing import Tuple, Generator, Iterable, Callable


Combination = Tuple[int, int, int]


def n_right_same_place(n: int, a: Combination, b: Combination) -> bool:
    digitpairs = zip(a, b)
    matches = sum(1 for pair in digitpairs if pair[0] == pair[1])
    return matches == n

def n_right_diff_place(n: int, a: Combination, b: Combination) -> bool:
    commondigits = set(a) & set(b)
    return (
        len(commondigits) == n and
        all(a.index(digit) != b.index(digit) for digit in commondigits)
    )

def all_wrong(a: Combination, b: Combination) -> bool:
    return len(set(a) & set(b)) == 0


def combinations() -> Generator[Combination, None, None]:
    for i in range(10):
        for j in range(10):
            for k in range(10):
                yield (i, j, k)


if __name__ == "__main__":
    filters: Iterable[Callable[[Combination], bool]] = (
        lambda c: n_right_same_place(1, (6, 8, 2), c),
        lambda c: n_right_diff_place(1, (6, 1, 4), c),
        lambda c: n_right_diff_place(2, (2, 0, 6), c),
        lambda c:          all_wrong(   (7, 3, 8), c),
        lambda c: n_right_diff_place(1, (3, 8, 0), c)
    )
    
    matches = filter(
        lambda c: all(f(c) for f in filters),
        combinations()
    )

    print(f"Matching Combinations: {'; '.join(map(str, matches))}")
