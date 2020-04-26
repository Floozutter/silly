"""
A module that names integers as attributes using English number words.
"""

from typing import Any, List


# Global constants.
LOWERBOUND = -1000  # inclusive
UPPERBOUND =  1001  # exclusive


# Helper function for concatenating English number words.
def concat(a: str, b: str, separator: str = " ") -> str:
    """Concatenates two English number words. Ignores a right-hand zero."""
    if b == "zero": return a
    else          : return a + separator + b

# Function for converting integers to English number words.
def numeralize(z: int) -> str:
    """Returns the integer argument as English number words."""
    # Case for negatives.
    if z < 0:     return "negative " + numeralize(-z)
    # Case for zero.
    elif z ==  0: return "zero"
    # Cases for small numbers.
    elif z ==  1: return "one"
    elif z ==  2: return "two"
    elif z ==  3: return "three"
    elif z ==  4: return "four"
    elif z ==  5: return "five"
    elif z ==  6: return "six"
    elif z ==  7: return "seven"
    elif z ==  8: return "eight"
    elif z ==  9: return "nine"
    elif z == 10: return "ten"
    elif z == 11: return "eleven"
    elif z == 12: return "twelve"
    elif z == 13: return "thirteen"
    elif z == 14: return "fourteen"
    elif z == 15: return "fifteen"
    elif z == 16: return "sixteen"
    elif z == 17: return "seventeen"
    elif z == 18: return "eighteen"
    elif z == 19: return "nineteen"
    # Cases for the tens.
    elif z == 20: return "twenty"
    elif z == 30: return "thirty"
    elif z == 40: return "forty"
    elif z == 50: return "fifty"
    elif z == 60: return "sixty"
    elif z == 70: return "seventy"
    elif z == 80: return "eighty"
    elif z == 90: return "ninety"
    # Cases for numbers within [21, 100).
    elif z < 100:
        tens, ones = divmod(z, 10)
        return concat(numeralize(tens*10), numeralize(ones), "-")
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
