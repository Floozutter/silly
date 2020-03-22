"""
Some various examples of mutual recursion.
"""

# INTEGER PARITY 
## From the first example on Wikipedia's "Mutual recursion" article.
## Note: This implementation fails on negative arguments.
def is_even(n: int) -> bool:
    if n == 0: return True
    else:      return is_odd(n-1)
def is_odd(n: int) -> bool:
    if n == 0: return False
    else:      return is_even(n-1)

# ALTERNATING BINARY STRING
## Checking if a string represting a binary number is in the form "101010...",
## where any two consecutive characters must be different.
def alternates_from_1(s: str) -> bool:
    if not s:       return True
    if s[0] != "1": return False
    else:           return alternates_from_0(s[1:])
def alternates_from_0(s: str) -> bool:
    if not s:       return True
    if s[0] != "0": return False
    else:           return alternates_from_1(s[1:])
