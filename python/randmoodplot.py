"""
A plotting companion to randmood.py.
"""

import matplotlib.pyplot as plt
from itertools import islice
from typing import Callable, Iterator


def plot_generator(
	title: str,
	genf: Callable[[float], Iterator[float]],
	n: int,
	p: float
) -> None:
	plot(
		title,
		range(n+1),
		list(islice(genf(p), n+1))
	)

def plot_solution(
	title: str,
	f: Callable[[int, float], float],
	n: int,
	p: float
) -> None:
	plot(
		title,
		range(n+1),
		[f(i, p) for i in range(n+1)]
	)

def plot(title: str, x, y) -> None:
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.set_title(title)
	ax.set_xlabel("n (seconds)")
	ax.set_ylabel("p (probability of happy)")
	ax.set_ylim(0, 1)
	ax.plot(x, y)
	fig.show()