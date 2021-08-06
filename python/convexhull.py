import math
import itertools
import functools
from typing import NamedTuple, Iterable, Sequence

class Point(NamedTuple):
    x: float
    y: float
    def norm(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)
    def __mul__(self, other: float) -> "Point":
        return Point(other * self.x, other * self.y)
    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)


class Triangle(NamedTuple):
    a: Point
    b: Point
    c: Point
    def contains(self, point: Point, epsilon: float = 0.000001) -> bool:
        shoelace = lambda a, b, c: abs((a.x-c.x)*(b.y-a.y) - (a.x-b.x)*(c.y - a.y)) / 2
        area = shoelace(self.a, self.b, self.c)
        subareas = (
            shoelace(point, self.a, self.b),
            shoelace(point, self.b, self.c),
            shoelace(point, self.c, self.a)
        )
        return sum(subareas) - area < epsilon

class ConvexHull:
    vertices: tuple[Point, ...]
    _angles: float
    _mean: Point
    def __init__(self, vertices: Sequence[Point]):
        if len(vertices) < 3:
            raise ValueError("at least 3 vertices needed")
        # compute mean
        xs, ys = zip(*vertices)
        self._mean = Point(sum(xs) / len(xs), sum(ys) / len(ys))
        # compute angles of mean-to-vertex vectors and sort them
        pairs = sorted(
            ((v, math.atan2(v.y - self._mean.y, v.x - self._mean.x)) for v in vertices),
            key = lambda pair: (pair[1], pair[0])
        )
        self.vertices, self._angles = zip(*pairs)
    def including(self, point: Point) -> "ConvexHull":
        if self.contains(point): return self
        # get closest vertex on hull
        angle = math.atan2(point.y - self._mean.y, point.x - self._mean.x)
        closest_index = min(
            enumerate(self._angles),
            key = lambda pair: abs(angle - pair[1])
        )[0]
        # search for counterclockwise-adjacent vertex
        i = closest_index
        while True:
            a, b, c = point, self.vertices[i], self.vertices[(i + 1) % len(self.vertices)]
            ba = a - b
            bc = c - b
            dx = (bc.x*ba.x + bc.y*ba.y) / ba.norm()
            dy = (bc.y*ba.x - bc.x*ba.y) / ba.norm()
            alpha = math.atan2(dy, dx)
            if alpha < 0:
                break
            i = (i + 1) % len(self.vertices)
        # search for clockwise-adjacent vertex
        j = closest_index
        while True:
            a, b, c = point, self.vertices[j], self.vertices[(j - 1) % len(self.vertices)]
            ba = a - b
            bc = c - b
            dx = (bc.x*ba.x + bc.y*ba.y) / ba.norm()
            dy = (bc.y*ba.x - bc.x*ba.y) / ba.norm()
            beta = math.atan2(dy, dx)
            if beta > 0:
                break
            j = (j - 1) % len(self.vertices)
        # build vertices
        vs = [point]
        while i != j:
            vs.append(self.vertices[i])
            i = (i + 1) % len(self.vertices)
        vs.append(self.vertices[i])
        return ConvexHull(vs)
    def contains(self, point: Point) -> bool:
        return any(t.contains(point) for t in self.triangles)
    @functools.cached_property
    def triangles(self) -> Sequence[Triangle]:
        return tuple(
            Triangle(self.vertices[0], self.vertices[i - 1], self.vertices[i])
            for i in range(2, len(self.vertices))
        )
    @classmethod
    def from_points(cls, points: Sequence[Point]) -> "ConvexHull":
        chull = cls(points[:3])
        for p in points[3:]:
            chull = chull.including(p)
        return chull

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import random
    # generate points
    points = tuple(
        Point(random.random(), random.random()) * 100
        for _ in range(random.randrange(7, 51))
    )
    # get convex hull
    chull = ConvexHull.from_points(points)
    # set up plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(-50, 150)
    ax.set_ylim(-50, 150)
    # plot points
    ax.scatter(*zip(*points), c = "blue")
    # plot convex hull
    vertices = chull.vertices
    closed = (*vertices, vertices[0])
    ax.plot(*zip(*closed), c = "red")
    # display plot
    plt.show()
