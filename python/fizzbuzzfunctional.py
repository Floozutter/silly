"""
An extensible solution to the FizzBuzz problem, in a functional style.
https://en.wikipedia.org/wiki/Fizz_buzz

Updated using Maciej Piróg's "FizzBuzz in Haskell by Embedding a
Domain-Specific Language"!
https://themonadreader.files.wordpress.com/2014/04/fizzbuzz.pdf
"""

from functools import reduce
from typing import NamedTuple, Callable, Iterable


class Rule(NamedTuple):
	subname: str
	predicate: Callable[[int], bool]


def make_namer(rules: Iterable[Rule]) -> Callable[[int], str]:
	"""
	Returns a namer constructed from the given rules.
	The namer will name an integer as a concatenation of every valid subname
	it fulfills from the rules. The order of the subnames corresponds to the
	order of the rules in the Iterable. However, if no subnames were
	fulfilled, the namer will default to naming the integer by its string
	value instead.
	"""
	def namer(z: int) -> str:
		"""Names the integer argument using the bound rules."""
		def test(rule: Rule, f: Callable[[str], str]) -> Callable[[str], str]:
			if rule.predicate(z):
				return lambda _: rule.subname + f("")
			else:
				return f
		return reduce(
			lambda f, g: lambda x: f(g(x)),
			map(
				lambda rule: lambda f: test(rule, f),
				rules
			)
		)(lambda s: s)(str(z))
	return namer


if __name__ == "__main__":
	fizzbuzz = make_namer((
		Rule("Fizz", lambda z: z % 3 == 0),
		Rule("Buzz", lambda z: z % 5 == 0)
	))
	
	for name in map(fizzbuzz, range(0, 100)):
		print(name)
