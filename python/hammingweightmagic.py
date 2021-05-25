"""
https://en.wikipedia.org/wiki/Hamming_weight
https://dl.acm.org/doi/10.1145/367236.367286
"""

from argparse import ArgumentParser
from typing import Iterator

def magic(z: int) -> Iterator[int]:
    while z:
        yield z
        z &= z - 1

def parse_args() -> int:
    parser = ArgumentParser()
    parser.add_argument("z", type = int, help = "integer to get the hamming weight of")
    z = parser.parse_args().z
    if z < 0:
        parser.error("z must be nonnegative!")
    return z

def main(z: int) -> None:
    steps = tuple(magic(z))
    for i, step in enumerate(steps):
        print(f"step {i}: {step:b}")
    print(f"the hamming weight of {z} is {len(steps)}")

if __name__ == "__main__":
    main(parse_args())
