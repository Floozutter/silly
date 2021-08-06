import math
import itertools
from typing import NamedTuple, Iterable, Sequence

class Point(NamedTuple):
    x: float
    y: float

def in_triangle(tri: tuple[Point, Point, Point], p: Point) -> bool:
    def shoelace(a: Point, b: Point, c: Point) -> float:
        return abs(
            (a.x - c.x) * (b.y - a.y) - (a.x - b.x) * (c.y - a.y)
        ) / 2
    a, b, c = tri
    area = shoelace(a, b, c)
    subareas = (
        shoelace(p, a, b),
        shoelace(p, b, c),
        shoelace(p, c, a)
    )
    return sum(subareas) <= area

def average(points: Iterable[Point]) -> Point:
    xs, ys = zip(*points)
    return Point(sum(xs) / len(xs), sum(ys) / len(ys))

def convex_hull(points: Sequence[Point]) -> Sequence[Point]:
    """returns the vertices of the convex hull for the given points"""
    assert len(points) > 3
    chull = points[:3]
    rest = points[3:]
    def aggregate(chull: Sequence[Point], point: Point) -> Sequence[Point]:
        #print(point)
        triangles = (
            (chull[0], chull[i - 1], chull[i])
            for i in range(2, len(chull))
        )
        if any(in_triangle(t, point) for t in triangles):
            return chull
        else:
            segments = itertools.combinations(chull, 2)
            triangles = ((point, *s) for s in segments)
            points = tuple((*chull, point))
            on_or_outs = tuple(
                tuple(p for p in points if p in t or not in_triangle(t, p))
                for t in triangles
            )
            #print(tuple(map(len, on_or_outs)))
            unordered = min(on_or_outs, key = len)
            center = average(unordered)
            def angle(p: Point) -> float:
                dx = p.x - center.x
                dy = p.y - center.y
                return math.atan2(dy, dx)
            return sorted(
                unordered,
                key = angle
            )
    #print(chull)
    for point in rest:
        chull = aggregate(chull, point)
        #print(chull)
    return chull

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import random
    # generate points
    points = tuple(
        Point(random.random(), random.random())
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
