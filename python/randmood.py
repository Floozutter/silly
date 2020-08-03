"""
A comparison of some solutions to Errichto's "Random Mood" problem.
The problem on Codeforces: https://codeforces.com/gym/102644/problem/A

"Limak is always either happy or sad. His mood switches with probability p
every second. If Limak is happy right now, what is the probability that he's
happy after n seconds?"
"""

from random import random
from math import prod, factorial
from itertools import islice
from typing import Iterator


def trial(n: int, p: float) -> bool:
	happy = True
	for _ in range(n):
		if random() < p:
			happy = not happy
	return happy

def simulate(trials: int, n: int, p: float) -> float:
	results: Iterator[bool] = (trial(n, p) for _ in range(trials))
	happies: int = sum(filter(None, results))
	return happies/trials


def generatorIterative(p: float) -> Iterator[float]:
	"""
	Returns an infinite stream of probabilities.
	The nth element of the stream (starting from zero) corresponds to the
	probability of being happy after n seconds.
	"""
	happy: float = 1  # Probability of being happy.
	while True:
		yield happy
		stay = (1 - p) * happy  # Probability of staying when happy.
		flip = p * (1 - happy)  # Probability of flipping when not happy.
		happy = stay + flip

def solutionIterative(n: int, p: float) -> float:
	"""
	The first solution I thought of.
	"""
	return next(islice(generatorIterative(p), n, None))


def solutionRecursive(n: int, p: float) -> float:
	"""
	Recursion!
	The recurrence relation:
		h[0] = 1,
		h[n] = (1 - p) h[n-1] + p (1 - h[n-1]) = (-2p + 1) h[n-1] + p.
	"""
	def recur(n: int, happy: float) -> float:
		return happy if n == 0 else recur(n-1, (-2*p + 1)*happy + p)
	return recur(n, 1)


def solutionClosed(n: int, p: float) -> float:
	"""
	A closed-form solution to solutionRecursive's recurrence relation.
	Derivation:
	Let q = (-2p + 1).
		h[0] = 1,
		h[n] = q h[n-1] + p.
	By iterating,
		h[1] = q + p,
		h[2] = q (q + p) + p = q^2 + pq + p,
		h[3] = q (q^2 + pq + p) + p = q^3 + pq^2 + pq + p,
		h[n] = q^n + p(q^(n-1) + q^(n-2) + ... + q^0).
	Because the term p(q^(n-1) + q^(n-2) + ... + q^0) is a geometric series,
		h[n] = q^n + p(1 - q^n)/(1 - q).
	Substituting q = (-2p + 1) and simplifying,
		h[n] = ((-2p + 1)^n + 1)/2.
	"""
	return ((-2*p + 1)**n + 1)/2


def solutionImitative(n: int, p: float) -> float:
	"""
	Reproduces a pattern in the expanded form of h[n]:
		h[0] = 1,
		h[1] = 1 - p,
		h[2] = 1 - 2p + 2p^2,
		h[3] = 1 - 3p + 6p^2 - 4p^3,
		h[4] = 1 - 4p + 12p^2 - 16p^3 + 8p^4,
		h[5] = 1 - 5p + 20p^2 - 40p^3 + 40p^4 - 16p^5,
		h[6] = 1 - 6p + 30p^2 - 80p^3 + 120p^4 - 96p^5 + 32p^6.
	"""
	def falling_factorial(start: int, factors: int) -> int:
		return prod(range(start, start-factors, -1))
	def term(i: int) -> float:
		sign = 1 if i % 2 == 0 else -1
		coef = max(1, 2**(i-1)) / factorial(i)
		return sign * coef * falling_factorial(n, i) * p**i
	return sum(map(term, range(n+1)))


if __name__ == "__main__":
	pass
