"""
ehe
"""

from argparse import ArgumentParser

def ehe(n: int) -> str:
    return "e" + "he"*n

def parse_args() -> int:
    parser = ArgumentParser(description = __doc__)
    parser.add_argument("n", type = int)
    return parser.parse_args().n

def main(n: int) -> None:
    print(ehe(n))

if __name__ == "__main__":
    main(parse_args())
