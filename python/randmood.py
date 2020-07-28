"""
A comparison of some solutions to Errichto's "Random Mood" problem.
The problem on Codeforces: https://codeforces.com/gym/102644/problem/A

"Limak is always either happy or sad. His mood switches with probability p
every second. If Limak is happy right now, what is the probability that he's
happy after n seconds?"
"""

from random import random
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


def solutionA(n: int, p: float) -> float:
	"""
	A simple solution that iterates over a single value in a loop.
	(The first solution I thought of.)
	"""
	happy = 1  # Probability of being happy.
	for _ in range(n):
		stay = happy * (1 - p)  # Probability of staying when happy.
		flip = (1 - happy) * p  # Probability of flipping when not happy.
		happy = stay + flip
	return happy


if __name__ == "__main__":
	pass