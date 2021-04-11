"""
names 80 cows from a newline-separated input file and a seed
"""

from random import Random
from argparse import ArgumentParser

def parse_args() -> tuple[str, str]:
    parser = ArgumentParser(description = __doc__)
    parser.add_argument("namesfilename", type = str, help = "name of file of names")
    parser.add_argument("seed", type = str, help = "seed for random")
    args = parser.parse_args()
    return args.namesfilename, args.seed

def main(namesfilename: str, seed: str) -> int:
    rng = Random(seed)
    with open(namesfilename, "r") as ifile:
        itext = ifile.read()
    names = tuple(itext.strip().split("\n"))
    for index, name in enumerate(rng.choices(names, k = 80)):
        print(f"0x{index:02x}: {name}")
    return 0

if __name__ == "__main__":
    exit(main(*parse_args()))
