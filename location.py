import sys
import math
import stdio
import random


class Location:

    # Construct self centered at (x, y) with charge q.
    def __init__(self, degree, minutes, seconds, cardinal):
        self.d = degree  # 1° = 60' = 3600"
        self.m = minutes  # 1' = (1/60)° = 0.01666667°
        self.s = seconds  # 1" = (1/3600)° = 2.77778e-4° = 0.000277778°
        self.card = cardinal  # (SWNE)) Lines of latitude range from 0° at the equator to 90°
        # Lines of longitude run from the north to the south start at 0° in Greenwich, England
        # and run to 180° West and East.

    # Return a string representation of self.
    def __str__(self):
        if str(self.card) == "E" or str(self.card) == "W":
            result = (f"{self.d:03d}") + '°' + str(self.m) + "'" + str(self.m) + '"' + str(self.card)
        else:
            result = (f"{self.d:02d}") + '°' + str(self.m) + "'" + str(self.m) + '"' + str(self.card)
        return result

    def randLocation(self, other):
        # latitude 0-90 S N
        # longtitdue 0-180 W E
        self.d = random.randrange(0, 90, 1)
        self.m = random.randrange(0, 60, 1)
        self.s = random.randrange(0, 60, 1)
        mylist = ["S", "N"]
        self.card = random.choice(mylist)

        other.d = random.randrange(0, 180, 1)
        other.m = random.randrange(0, 60, 1)
        other.s = random.randrange(0, 60, 1)
        mylist_la = ["W", "E"]
        other.card = random.choice(mylist_la)


# -----------------------------------------------------------------------


def main():
    # test
    # Moscow 55°48'20.5"N 37°39'10.2"E. Paris 48°51'36.1"N 2°23'48.7"E.

    longtitude_start = Location(55, 48, 20, 'N')
    lattitude_start = Location(37, 39, 10, 'E')

    longtitude_finish = Location(48, 51, 36, 'N')
    latitude_finish = Location(2, 23, 48, 'E')
    random_la = Location(0, 0, 0, "S")
    random_lo = Location(0, 0, 0, "N")
    random_la.randLocation(random_lo)
    print(random_la)
    print(random_lo)

    # print(longtitude_start)
    # print(lattitude_start)
    # print(longtitude_finish)
    # print(latitude_finish)
    # print(distanceTo( longtitude_start,lattitude_start,  longtitude_finish, latitude_finish))


if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------
