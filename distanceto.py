import math
from location import Location

"""
   distanceTo()
    Great circle. Compose a program that accepts four floats as command-line
   arguments—x1, y1, x2, and y2—(the latitude and longitude, in degrees, of two
   points on the earth) and writes the great-circle distance between them. The 
   greatcircle distance d (in nautical miles) is given by the following equation:
   d = 60 arccos(sin(x1) sin(x2)  cos(x1) cos(x2) cos(y1  y2))
   Note that this equation uses degrees, whereas Python’s trigonometric functions use
   radians. Use math.radians() and math.degrees() to convert between the two.
   Use your program to compute the great-circle distance between Paris (48.87° N
   and 2.33° W) and San Francisco (37.8° N and 122.4° W). 
   a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
    `c = 2 ⋅ atan2( √a, √(1−a) )
    d = R ⋅ c
    where	φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);
    note that angles need to be in radians to pass to trig functions!


   """


def distanceTo(lo1, la1, lo2, la2):
    y1 = math.radians((la1.d) + (la1.m / 60) + (la1.s / 3600))
    x1 = math.radians((lo1.d) + (lo1.m / 60) + (lo1.s / 3600))
    y2 = math.radians((la2.d) + (la2.m / 60) + (la1.s / 3600))
    x2 = math.radians((lo2.d) + (lo2.m / 60) + (lo2.s / 3600))

    R = 6371e3
    # fi1 = y1 * math.pi / 180
    fi1 = y1
    # fi2 = y2 * math.pi / 180
    fi2 = y2
    deltafi = (y2 - y1)
              # * math.pi / 180
    deltalafa = (x2 - x1)
                # * math.pi / 180

    a = math.sin(deltafi / 2) * math.sin(deltafi / 2) + math.cos(fi1) \
        * math.cos(fi2) * math.sin(deltalafa / 2) * math.sin(deltafi / 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # d = (R * c) / 1000
    d = (math.degrees(c)*60*1.852)

    return d  # converts degrees to m


lattitude_start = Location(12, 2, 58, 'W')
longtitude_start = Location(45, 3, 32, 'S')

latitude_finish = Location(44, 3, 32, 'S')
longtitude_finish = Location(18, 44, 30, 'E')

# random_la = Location(0, 0, 0, "S")
# random_lo = Location(0, 0, 0, "N")
# lattitude_start.randLocation(longtitude_start)
print(lattitude_start)
print(longtitude_start)

# latitude_finish.randLocation(longtitude_finish)
print(latitude_finish)
print(longtitude_finish)

print(distanceTo(longtitude_start, lattitude_start, longtitude_finish, latitude_finish))
