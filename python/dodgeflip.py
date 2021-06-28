"""
use coin flips to choose who dodges!
"""

import random
import math
from enum import Enum

class CoinFlip(Enum):
    TAILS = "0"
    HEADS = "1"

def flip_coin() -> CoinFlip:
    return CoinFlip.HEADS if random.getrandbits(1) else CoinFlip.TAILS

def choose_who_dodges(players: frozenset[str]) -> str:
    # start by enumerating all the players with indices (for n players, number them from 0 to n-1)
    n = len(players)
    enumerated_players = tuple(players)
    # then, figure out the number of coin flips needed per trial, k = ceil(log2(n))
    k = math.ceil(math.log2(n))
    while True:
        # flip your coin k times and remember the results and their order
        flips = (flip_coin() for _ in range(k))
        # construct a binary number by interpreting each coin flip as a bit (0 or 1)
        binstring = "".join(coin.value for coin in flips)
        # if your binary number is a valid index, then the player with that index is chosen!
        index = int(binstring, 2)
        if index < n:
            return enumerated_players[index]
        # otherwise, try again...

if __name__ == "__main__":
    print(choose_who_dodges({"bonk", "Definitely Floozutter", "i look like phoenix irl", "mikle"}))
