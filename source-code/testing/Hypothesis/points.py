import math
from hypothesis import given, strategies as st


class Point:

    _x: float
    _y: float

    def __init__(self, x: float, y: float):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = float(x)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = float(y)

    def __repr__(self):
        return f'Point({self._x}, {self._y})'

    def __str__(self):
        return f'({self._x}, {self._y})'

    def distance(self, other):
        return math.sqrt((self._x - other._x)**2 + (self._y - other._y)**2)

    def is_on_line(self, p1, p2):
        return math.isclose(self.y - ((p2.y - p1.y)*self.x - p1.x*p2.y + p2.x*p1.y)/(p2.x - p1.x), 0.0)


def test_distance():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert math.isclose(p1.distance(p2), 5.0)


@given(x1=st.floats(), y1=st.floats(), x2=st.floats(), y2=st.floats())
def test_is_on_line(x1: float, y1: float, x2: float, y2: float):
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p = Point((x1 + x2)/2, (y1 + y2)/2)
    assert p.is_on_line(p1, p2)
    assert p1.is_on_line(p1, p2)
    assert p2.is_on_line(p1, p2)
