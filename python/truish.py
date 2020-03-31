"""
A module that provides a value somewhere between True and False... Truish!
"""

from random import random
from typing import Any, List


# Global constants.
TRUISHNAME = "Truish"  # Name of the Truish attribute of this module.
TRUISHNESS = 0.75      # Probability of Truish being True.

# Names of public objects.
__all__ = ["TRUISHNAME", "TRUISHNESS", "chance"]


# Helper function for evaluating the value of Truish.
def chance(truthrate: float) -> bool:
    """Returns a Boolean with the probability of truthrate of being True."""
    return random() < truthrate


# Define Truish as an attribute of this module.
## This module's __getattr__.
def __getattr__(name: str) -> Any:
    if name == TRUISHNAME:
        return chance(TRUISHNESS)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    
## This module's __dir__.
def __dir__() -> List[str]:
    return sorted(__all__ + [TRUISHNAME])


# Driver for testing.
if __name__ == "__main__":
    # Get a reference to this module.
    from sys import modules
    thismodule = modules[__name__]
    
    # Test the value of Truish repeatedly.
    trials = 10
    print(f"Testing the value of {TRUISHNAME} {trials} times.")
    for i in range(trials):
        print(f"{i+1:>{len(str(trials))}}: {TRUISHNAME} == ", end="")
        print(getattr(thismodule, TRUISHNAME))

    # See the names of valid attributes for this module.
    print(f"\nThis module's attributes: {dir(thismodule)}")
