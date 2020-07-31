"""
A comparison of some solutions to Errichto's "Random Mood" problem.
The problem on Codeforces: https://codeforces.com/gym/102644/problem/A

"Limak is always either happy or sad. His mood switches with probability p
every second. If Limak is happy right now, what is the probability that he's
happy after n seconds?"
"""

from random import random
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


def generatorA(p: float) -> Iterator[float]:
	"""
	Returns an infinite stream of probabilities.
	The nth element of the stream (starting from zero) corresponds to the
	probability of being happy after n seconds.
	"""
	happy: float = 1  # Probability of being happy.
	while True:
		yield happy
		stay = happy * (1 - p)  # Probability of staying when happy.
		flip = (1 - happy) * p  # Probability of flipping when not happy.
		happy = stay + flip

def solutionA(n: int, p: float) -> float:
	"""
	The first solution I thought of.
	"""
	return next(islice(generatorA(p), n, None))


def solutionB(n: int, p: float) -> float:
	"""
	Recursion!
	"""
	def recur(n: int, happy: float) -> float:
		return happy if n == 0 else recur(n-1, happy*(1-p) + (1-happy)*p)
	return recur(n, 1)


def solutionC(n: int, p: float) -> float:
	"""
	Searching for a pattern...
	"""
	if   n == 0: return 1
	elif n == 1: return 1 - p
	elif n == 2: return 1 - 2*p + 2*p**2
	elif n == 3: return 1 - 3*p + 6*p**2 - 4*p**3
	elif n == 4: return 1 - 4*p + 12*p**2 - 16*p**3 + 8*p**4
	elif n == 5: return 1 - 5*p + 20*p**2 - 40*p**3 + 40*p**4 - 16*p**5
	elif n == 6: return 1 - 6*p + 30*p**2 - 80*p**3 + 120*p**4 - 96*p**5 + 32*p**6
	else:
		return -1


if __name__ == "__main__":
	pass