# -----------------------------------------------------------------------
# vector.py
# -----------------------------------------------------------------------

import math
import stdio
import stdarray


# -----------------------------------------------------------------------

class Vector:

    # Construct a new Vector object with numeric Cartesian coordinates
    # given in array a.
    def __init__(self, a, b):
        # Make a defensive copy to ensure immutability.

        self._coord_a = float(a)  # Cartesian coordinates
        self._coord_b = float(b)
        # self._n = len(a)  # Dimension.

    # Return the 0th or 1st Cartesian coordinate of self.
    def __getitem__(self, i):
        if i == 0:
            return self._coord_a
        if i == 1:
            return self._coord_b
        else:
            print("returns the first or the second coordinate only")

    # Return the sum of self and Vector object other.
    def __add__(self, other):
        a = self._coord_a + other._coord_a
        b = self._coord_b + other._coord_b
        return Vector(a, b)

    # Return the difference of self and Vector object other.
    def __sub__(self, other):
        a = self._coord_a - other._coord_a
        b = self._coord_b - other._coord_b
        return Vector(a, b)

    # Return the product of self and numeric object alpha.
    def scale(self, alpha):
        a = alpha * self._coord_a
        b = alpha * self._coord_b
        return Vector(a, b)

    # Return the inner product of self and Vector object other.
    def dot(self, other):
        result = self._coord_a * other._coord_a + self._coord_b * other._coord_b
        return result

    # Return the magnitude, that is, the Euclidean norm, of self.
    def __abs__(self):
        return math.sqrt(self.dot(self))

    # Return the unit vector of self.
    def direction(self):
        return self.scale(1.0 / abs(self))

    # Return a string representation of self.
    def __str__(self):
        return str(self._coord_a)+" "+str(self._coord_b)




# -----------------------------------------------------------------------

# For testing.
# Create and use some Vector objects.

def main():
    Coords_1 = (1.1, 2.1)
    Coords_2 = (5.1, 2.1)

    x = Vector(Coords_1[0], Coords_1[1])
    y = Vector(Coords_2[0], Coords_2[1])

    stdio.writeln('Coords_1        = ' + str(x))
    stdio.writeln('Coords_2        = ' + str(y))
    stdio.writeln('x + y    = ' + str(x + y))
    stdio.writeln('10x      = ' + str(x.scale(10.0)))
    stdio.writeln('|x|      = ' + str(abs(x)))
    stdio.writeln('<x, y>   = ' + str(x.dot(y)))
    stdio.writeln('|x - y|  = ' + str(abs(x - y)))


if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------

# python vector.py
# x        = [1.0, 2.0, 3.0, 4.0]
# y        = [5.0, 2.0, 4.0, 1.0]
# x + y    = [6.0, 4.0, 7.0, 5.0]
# 10x      = [10.0, 20.0, 30.0, 40.0]
# |x|      = 5.477225575051661
# <x, y>   = 25.0
# |x - y|  = 5.0990195135927845
