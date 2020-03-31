"""
A module that names integers as attributes using English number words.
"""

from typing import Any, List


# Global constants.
LOWERBOUND = -1000  # inclusive
UPPERBOUND =  1001  # exclusive


# Helper function for converting integers to English number words.
def numeralize(z: int) -> str:
    """Returns the integer argument as English number words."""
    if z < 0:    return "negative " + numeralize(-z)
    elif z == 0: return "zero"
    raise NotImplementedError()

# Helper function for converting numerals to valid attribute names.
def attributify(numeral: str) -> str:
    """Returns the numeral string argument as a valid attribute name."""
    return numeral.replace(" ", "").replace("-", "")


# Generate dictionary of numeral attributes by brute force.
NUMERALS = dict(
    (attributify(numeralize(i)), i) for i in range(LOWERBOUND, UPPERBOUND)
)

# Make list of names of public objects.
__all__ = sorted(
    ["LOWERBOUND", "UPPERBOUND", "numeralize", "attributify"] +
    list(NUMERALS.keys())
)


# Define numeral attributes.
## This module's __getattr__.
def __getattr__(name: str) -> Any:
    if name in NUMERALS:
        return NUMERALS[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

## This module's __dir__.
def __dir__() -> List[str]:
    return __all__


# Driver for testing.
if __name__ == "__main__":
    # Get a reference to this module.
    from sys import modules
    thismodule = modules[__name__]

    # See the names of valid attributes for this module.
    print(f"\nThis module's attributes: {dir(thismodule)}")
