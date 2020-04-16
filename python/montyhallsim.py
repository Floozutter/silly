"""
A loose simulation of the Monty Hall problem in Python.
"""

from random import randrange, sample
from typing import Tuple

Prize = bool
GOAT = False
CAR = True


def make_doors(doorcount: int, car_index: int) -> Tuple[Prize]:
    """Returns a representation of the doors in the Monty Hall Problem."""
    return tuple(CAR if i == car_index else GOAT for i in range(doorcount))

def play(doorcount: int, switch: bool) -> Prize:
    """Runs a trial of the Monty Hall problem and returns the Prize."""
    # Make the doors with a randomly generated index for the winning door.
    doors = make_doors(doorcount, randrange(doorcount))
    
    # Randomly generate the player's first choice.
    firstchoice = randrange(doorcount)

    # Generate every revealable door.
    # A door is revealable if it contains a goat and is not the first choice.
    revealable = tuple(
        i for i, prize in enumerate(doors) if (
            i != firstchoice and prize == GOAT
        )
    )

    # Reveal doors so that one door remains apart from the first choice.
    revealed = sample(revealable, doorcount - 2)

    # Get the index of the final remaining door.
    otherchoice = next(iter(
        set(range(doorcount)) - set(revealed) - {firstchoice}
    ))

    # Choose between the player's first choice and the other choice.
    finalchoice = otherchoice if switch else firstchoice

    # Return the Prize corresponding to the final choice.
    return doors[finalchoice]


def test(doorcount: int, switch: bool, trials: int) -> bool:
    """Returns a win rate for the Monty Hall problem with repeated trials."""
    wins = sum(int(play(doorcount, switch) == CAR) for _ in range(trials))
    return wins/trials


if __name__ == "__main__":
    trials = 10000
    
    # Test always switching with 3 doors.
    print(f"{3:>3} Doors | Always Switch: ", end="")
    print(f"{test(3, True, trials):%}")

    # Test always switching with 100 doors.
    print(f"{100:>3} Doors | Always Switch: ", end="")
    print(f"{test(100, True, trials):%}")
