import stddraw
import stdio
import sys


class Rectangle:
    # Create rectangle with center (x, y),
    # width w, and height h.
    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._width = w
        self._height = h
        # clockwise from X1Y1 to X4Y4 coordinates of the square
        self._coordX1 = x
        self._coordY1 = y

        self._coordX2 = x
        self._coordY2 = y + h

        self._coordX3 = x + w
        self._coordY3 = y + h

        self._coordX4 = x + w
        self._coordY4 = y

    # The area of self.
    def area(self):
        return (self._width) * (self._height)

    # The perimeter of self.
    def perimeter(self):
        return (self._width) * 2 + (self._height) * 2

    # True if self contains other; False otherwise.
    def contains(self, other):
        if self.contain_dot(other._coordX1, other._coordY1) \
                and self.contain_dot(other._coordX2, other._coordY2) \
                and self.contain_dot(other._coordX3, other._coordY3) \
                and self.contain_dot(other._coordX4, other._coordY4):
            return True
        else:
            return False

    def contain_dot(self, x, y):
        if self._x + self._width > x > self._x \
                and self._y + self._height > y > self._y:
            return True
        else:
            return False


    # True if self intersects other; False otherwise.
    def intersects(self, other):
        '''
        calculate min X Y for both squares (square around both)
        '''


        return True

    #     # compare horizontal lines
    #     if self.contains(other):
    #         return False
    #     if other.contains(self):
    #         return False
    #
    #     if (self._coordX1 + self._width > other._coordX1 > self._coordX1) \
    #             and other._coordY1 + other._height > self._coordY1 + self._height:
    #         return True
    #     if (self._coordY1 + self._height > other._coordY1 > self._coordY1) \
    #             and other._coordX1 + other._width > self._coordX1 + self._width:
    #         return True
    #
    #     if (self.contain_dot(other._coordX1, other._coordY1)
    #         or self.contain_dot(other._coordX2, other._coordY2)
    #         or self.contain_dot(other._coordX3, other._coordY3)
    #         or self.contain_dot(other._coordX4, other._coordY4)) \
    #             and (not self.contain_dot(other._coordX1, other._coordY1)) \
    #             or not (self.contain_dot(other._coordX2, other._coordY2)) \
    #             or not (self.contain_dot(other._coordX3, other._coordY3)) \
    #             or not (self.contain_dot(other._coordX4, other._coordY4)):
    #         return True
    #     if self.contain_dot(other._coordX1, other._coordY1) \
    #             or self.contain_dot(other._coordX2, other._coordY2) \
    #             or self.contain_dot(other._coordX3, other._coordY3) \
    #             or self.contain_dot(other._coordX4, other._coordY4):
    #         return True
    #     else:
    #         return False
    #
    # # Draw self on stddraw
    def draw(self):
        stddraw.rectangle(self._x, self._y, self._width, self._height)


def main():
    stddraw.setXscale(0, 10)
    stddraw.setYscale(0, 10)
    # 0.2, 0.3, 0.4, 0.4
    # 0.3, 0.4, 0.2, 0.2

    rectangle1 = Rectangle(2, 2, 2, 2)
    rectangle2 = Rectangle(3, 5, 2, 2)
    rectangle1.draw()
    rectangle2.draw()

    print(rectangle1.contains(rectangle2))
    print(rectangle2.contains(rectangle1))
    print(rectangle1.intersects(rectangle2))
    print(rectangle2.intersects(rectangle1))

    print(rectangle1.area())
    print(rectangle2.area())
    stddraw.show()


if __name__ == '__main__':
    main()
