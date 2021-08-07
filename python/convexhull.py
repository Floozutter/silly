import math
import functools
from typing import Any, Optional, NamedTuple, Sequence

class Point(NamedTuple):
    x: float
    y: float
    def norm(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)
    def __mul__(self, other: float) -> "Point":
        return Point(other * self.x, other * self.y)
    def __add__(self, other: Any) -> "Point":
        if not isinstance(other, Point): raise ValueError("oops")
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other: "Point") -> "Point":
        return Point(self.x - other.x, self.y - other.y)

def angle_abc(a: Point, b: Point, c: Point) -> float:
    ba = a - b
    bc = c - b
    dx = (bc.x*ba.x + bc.y*ba.y) / ba.norm()
    dy = (bc.y*ba.x - bc.x*ba.y) / ba.norm()
    return math.atan2(dy, dx)

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
    _angles: tuple[float, ...]
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
        # search for counterclockwise-adjacent vertex's concave angle
        i = closest_index
        while angle_abc(point, self.vertices[i], self.vertices[(i+1) % len(self.vertices)]) >= 0:
            i = (i+1) % len(self.vertices)
        # search for clockwise-adjacent vertex's concave angle
        j = closest_index
        while angle_abc(point, self.vertices[j], self.vertices[(j-1) % len(self.vertices)]) <= 0:
            j = (j-1) % len(self.vertices)
        # stitch together vertices
        vs = [point]
        while i != j:
            vs.append(self.vertices[i])
            i = (i+1) % len(self.vertices)
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


def parse_args() -> tuple[int, Optional[str]]:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--interval", type = int, default = 500)
    parser.add_argument("--seed", type = str, default = None)
    args = parser.parse_args()
    return args.interval, args.seed

def main(interval: int, seed: Optional[str]) -> None:
    import matplotlib.pyplot
    import matplotlib.animation
    import numpy
    import random
    # generate points
    r = random.Random(seed)
    points = tuple(
        Point(r.random(), r.random()) * 100
        for _ in range(r.randrange(7, 51))
    )
    # set up plot
    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim(-50, 150)
    ax.set_ylim(-50, 150)
    ax.scatter(*zip(*points), c = "blue")
    line ,= ax.plot((), (), c = "red")
    included = ax.scatter((), (), c = "red")
    remaining = ax.scatter((), (), c = "blue")
    # animate plot
    def update(i: int):
        if i < 3:
            line.set_data((), ())
        else:
            chull = ConvexHull.from_points(points[:i])
            closed = (*chull.vertices, chull.vertices[0])
            line.set_data(*zip(*closed))
        included.set_offsets(points[:i] or numpy.empty(shape = (0, 2)))
        remaining.set_offsets(points[i:] or numpy.empty(shape = (0, 2)))
        return line, included, remaining
    ani = matplotlib.animation.FuncAnimation(
        fig,
        update,
        frames = range(len(points) + 1),
        interval = interval,
        blit = True
    )
    matplotlib.pyplot.show()

if __name__ == "__main__":
    main(*parse_args())
