'''Module for working with points in 2D
'''

import math


class Point:
    '''Class that represents points in a 2D space
    '''

    def __init__(self, x_value, y_value):
        '''Create a new point at the given position

        Parameters
        ----------
        x: float
            x-coordinate of the point
        y: float
            y-coordinate of the point

        Examples
        --------
        >>> Point(3.1, 5.6)
        (3.1, 5.6)
        '''
        self._x = float(x_value)
        self._y = float(y_value)

    @property
    def x(self):
        '''Get the x-coordinate of the point

        Returns
        -------
        float
            x-coordinate of the point

        Examples
        --------
        >>> p = Point(3.1, 5.6)
        >>> p.x
        3.1
        '''
        return self._x

    @x.setter
    def x(self, value):
        '''Set the x-coordinate of the point

        Parameters
        ----------
        x: float
            x-coordinate to set

        Examples
        --------
        >>> p = Point(3.1, 5.6)
        >>> p.x = 1.0
        >>> p.x
        1.0
        '''
        self._x = float(value)

    @property
    def y(self):
        '''Get the y-coordinate of the point

        Returns
        -------
        float
            y-coordinate of the point

        Examples
        --------
        >>> p = Point(3.1, 5.6)
        >>> p.y
        5.6
        '''
        return self._y

    @y.setter
    def y(self, value):
        '''Set the y-coordinate of the point

        Parameters
        ----------
        y: float
            y-coordinate to set

        Examples
        --------
        >>> p = Point(3.1, 5.6)
        >>> p.y = 1.0
        >>> p.y
        1.0
        '''
        self._y = float(value)

    @property
    def coords(self):
        '''Get the coordinates of the point as a tuple

        Returns
        -------
        tuple[float, float]
            coordinate of the point

        Examples
        --------
        >>> p = Point(3.1, 5.6)
        >>> p.coords
        (3.1, 5.6)
        '''
        return (self.x, self.y)

    @coords.setter
    def coords(self, value):
        '''Modify to coordinates of the point

        Parameters
        ----------
        value: tuple[float, float]
            tuple with the new coordinates for the point

        Examples
        --------
        >>> p = Point(3.1, 5.6)
        >>> p.coords = (1.0, -1.0)
        >>> p.coords
        (1.01, -1.0)
        '''
        self._x, self._y = value

    def distance(self, other):
        '''Compute the distance between the point and another point

        Parameters
        ----------
        p: Point
            point to compute the Euclidean distance to

        Returns
        -------
        float
            distance between the two points

        Examples
        --------
        >>> p, q = Point(3.0, 0.0), Point(0.0, 4.0)
        >>> import math
        >>> math.isclose(5.0, p.distance(q))
        True
        '''
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self):
        '''Generate a non-ambiguous string representation of the
        point

        Returns
        -------
        str
            string representation of the point

        Examples
        --------
        >>> p = Point(3.1, 5.6)
        >>> repr(p)
        (3.1, 5.6)
        '''
        return f'({self.x}, {self.y})'


if __name__ == '__main__':
    import doctest
    doctest.testmod()
