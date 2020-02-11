"""
An extensible solution to the FizzBuzz problem, in a functional style.

https://en.wikipedia.org/wiki/Fizz_buzz
"""

from typing import Callable, NamedTuple, Iterable


IntChecker = Callable[[int], bool]  # checks if an integer passes a condition
IntNamer   = Callable[[int], str]   # names an integer by some rules
class Rule(NamedTuple):             # associates a subname to a condition
    subname: str
    condition: IntChecker 


def make_namer(rules: Iterable[Rule]) -> IntNamer:
    """
    Returns an IntNamer closure from an Iterable of Rules.

    The IntNamer will name an integer as a concatenation of every valid
    subname it fulfills from the Iterable of Rules.
    
    The order of the subnames in an int's full name corresponds to the order
    of the Rules in the Iterable.
    """
    
    def namer(z: int) -> str:
        """
        Names the integer argument using the bound List of Rules.
        """
        # make the full name from the subnames the integer fulfills
        name = "".join(r.subname for r in rules if r.condition(z))
        
        if name:  # the integer fulfills at least one subname
            return name
        
        # when the integer fulfills no subnames,
        # just name the integer by its value instead
        return str(z)
    
    return namer


if __name__ == "__main__":
    # make the classic FizzBizz namer
    fizzbuzz = make_namer((
        Rule("Fizz", lambda z: z % 3 == 0),
        Rule("Buzz", lambda z: z % 5 == 0)
    ))

    # name the integers within the range [1, 100] with fizzbuzz, then print
    for name in map(fizzbuzz, range(1, 101)):
        print(name)
