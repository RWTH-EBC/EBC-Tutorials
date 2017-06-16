class Point(object):
    """
    Point class
    """

    #  Initialize Point object with x and y input parameters
    def __init__(self, x, y):
        """
        Constructor of point object

        Parameter
        ---------
        x : float
            x-coordinate in m
        y : float
            y-coordinate in m
        """

        #  Hand over x and y as attributes to point object (self)
        self.x = x
        self.y = y

    def get_position_tuple(self):
        """
        Returns position tuple of point object

        Returns
        -------
        pos : tuple (of floats)
            Position tuple, format (x, y)
            x : float
                 x-coordinate in m
            y : float
                y-coordinate in m
        """
        pos = (self.x, self.y)
        return pos

    def calc_distance_to_other_point(self, other_point):
        """
        Calculates distance to other point.

        Parameters
        ----------
        other_point : Point object
            Point object (of EBC Python Tutorial)

        Returns
        -------
        distance : float
            Distance between two point objects
        """
        distance = ((self.y - other_point.y) ** 2 +
                    (self.x - other_point.x) ** 2) ** (1./2)
        return distance

if __name__ == '__main__':

    #  Generate two point objects
    point_1 = Point(0, 0)
    point_2 = Point(5, 10)

    #  Execute method get_position_tuple() of both point objects
    pos_1 = point_1.get_position_tuple()
    pos_2 = point_2.get_position_tuple()

    #  Print results (position tuples)
    print('Position tuple of point 1:', pos_1)
    print('Position tuple of point 2:', pos_2)

    #  Get x-coordinate of point 1
    x_coord = point_1.x
    print('x-coordinate of point 1 is:', x_coord)

    #  Calculate distance between point 1 and 2
    dist = point_1.calc_distance_to_other_point(point_2)
    print('Distance between point 1 and 2 is:', round(dist, 2))
