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
    def __init__(self, a):
        # Make a defensive copy to ensure immutability.
        self._coords = a[:]  # Cartesian coordinates
        self._n = len(a)  # Dimension.

    # Return the ith Cartesian coordinate of self.
    def __getitem__(self, i):
        return self._coords[i]

    # Return the sum of self and Vector object other.
    def __add__(self, other):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = self._coords[i] + other._coords[i]
        return Vector(result)

    # Return the difference of self and Vector object other.
    def __sub__(self, other):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = self._coords[i] - other._coords[i]
        return Vector(result)

    # Return the product of self and numeric object alpha.
    def scale(self, alpha):
        result = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result[i] = alpha * self._coords[i]
        return Vector(result)

    # Return the inner product of self and Vector object other.
    def dot(self, other):
        result = 0
        for i in range(self._n):
            result += self._coords[i] * other._coords[i]
        return result

    # Return the magnitude, that is, the Euclidean norm, of self.
    def __abs__(self):
        return math.sqrt(self.dot(self))

    # Return the unit vector of self.
    def direction(self):
        return self.scale(1.0 / abs(self))

    # Return a string representation of self.
    def __str__(self):
        return str(self._coords)

    # Return the dimension of self.
    def __len__(self):
        return self._n


class Particle(Vector):
    def __init__(self, position, velocity, mass):
        self._position = Vector(position[:])  # Cartesian coordinates
        self._velocity = Vector(velocity[:])
        self._m = mass
        self._n = len(position)
        # super(Particle, self).__init__(position)
        # super(Particle, self).__init__(velocity)

    def __str__(self):
        return str(self._position) + " " + str(self._velocity) + " " + str(self._m)
    def __add__(self, other):
        result_pos = stdarray.create1D(self._n, 0)
        result_vel = stdarray.create1D(self._n, 0)
        for i in range(self._n):
            result_pos[i] = self._position[i] + other._position[i]
            result_vel[i] = self._velocity[i] + other._velocity[i]
            result_mass = self._m+other._m
        return Particle(result_pos, result_vel,result_mass)

    def kinetic(self):
        v= self._velocity
        energy = (self._m)/2*(v[0]**2+v[1]**2+v[2]**2)
        return energy

# -----------------------------------------------------------------------

# For testing.
# Create and use some Vector objects.

def main():
    # xCoords = [1.0, 2.0, 3.0, 4.0]
    # yCoords = [5.0, 2.0, 4.0, 1.0]
    #
    # x = Vector(xCoords)
    # y = Vector(yCoords)
    #
    # stdio.writeln('x        = ' + str(x))
    # stdio.writeln('y        = ' + str(y))
    # stdio.writeln('x + y    = ' + str(x + y))
    # stdio.writeln('10x      = ' + str(x.scale(10.0)))
    # stdio.writeln('|x|      = ' + str(abs(x)))
    # stdio.writeln('<x, y>   = ' + str(x.dot(y)))
    # stdio.writeln('|x - y|  = ' + str(abs(x - y)))
    pos = [1, 2, 3]
    vel = [3, 2, 1]
    mass = 3
    a = Particle(pos, vel, mass)
    b = Particle([1, 1, 1], [2, 2, 2], 6)
    cv = a+b
    print(cv)
    print(cv.kinetic())

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
