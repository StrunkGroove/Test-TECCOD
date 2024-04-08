class Point:
    """
    Represents a point in two-dimensional space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value: float):
        self._x = value
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value: float):
        self._y = value

    def distance_to(self, other_point: 'Point') -> float:
        """
        Calculates the distance between the current point 
        and another point in two-dimensional space.

        Args:
            other_point (Point): The other point to which the distance needs 
            to be calculated.

        Returns:
            float: The distance between the current point and the other point.

        Example:
            >>> point1 = Point(1, 2)
            >>> point2 = Point(4, 6)
            >>> distance = point1.distance_to(point2)
            >>> print(distance)
            5.0
        """
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return (dx ** 2 + dy ** 2) ** 0.5
