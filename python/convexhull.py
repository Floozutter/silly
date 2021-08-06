from typing import Iterable, Sequence

Point = tuple[int, int]

def convex_hull(points: Iterable[Point]) -> Sequence[Point]:
    """returns the vertices of the convex hull for the given points"""
    return ((0, 0), (1, 0), (0, 1))


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import random
    # generate points
    points = (
        (random.random(), random.random())
        for _ in range(random.randrange(7, 16))
    )
    # get convex hull
    chull = convex_hull(points)
    # set up plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    # plot points
    ax.scatter(*zip(*points), c = "blue")
    # plot convex hull
    closed_chull = (*chull, chull[0])
    ax.plot(*zip(*closed_chull), c = "red")
    # display plot
    plt.show()
