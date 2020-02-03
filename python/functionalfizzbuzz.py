"""
An extensible solution to the FizzBuzz problem, in a functional style.

https://en.wikipedia.org/wiki/Fizz_buzz
"""

from typing import Callable, NamedTuple, List


IntChecker = Callable[[int], bool]  # checks if an integer passes a condition
IntNamer   = Callable[[int], str]   # names an integer by some rules
class Rule(NamedTuple):             # associates a subname to a condition
    subname: str
    condition: IntChecker 


def make_namer(rules: List[Rule]) -> IntNamer:
    """
    Returns an IntNamer closure from a list of Rules.

    The IntNamer will name an integer as a concatenation of every valid
    subname it fulfills from the List of Rules.
    
    The order of the subnames in an int's full name corresponds to the order
    of the Rules in the List of Rules.
    """
    
    def namer(z: int) -> str:
        """
        Names the integer argument using the bound List of Rules.
        """
        # get the subnames the integer fulfills
        subnames = [r.subname for r in rules if r.condition(z)]
        
        if subnames:  # the integer fulfills at least one subname
            return "".join(subnames)
        
        # when the integer fulfills no subnames,
        # name the integer by its value
        return str(z)
    
    return namer


if __name__ == "__main__":
    # make the classic FizzBizz namer
    fizzbuzz = make_namer([
        Rule("Fizz", lambda z: z % 3 == 0),
        Rule("Buzz", lambda z: z % 5 == 0)
    ])

    # name the integers within the range [1, 100] with fizzbuzz, and print
    print("\n".join(map(fizzbuzz, range(1, 101))))
