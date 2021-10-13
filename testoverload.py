# -----------------------------------------------------------------------
# counter.py
# -----------------------------------------------------------------------

import sys
import stdio
# import stdarray
import stdrandom


class Newclass:

    def __init__(self, id, name):
        self._name = name # Counter name
        self._id = id

    def __str__(self):
        return str(self._name) + ': ' + str(self._id)

    def __add__(self, other):
        _n = self._name + " " + other._name
        _i = self._id + other._id
        k = Newclass(_n, _i)
        return k

def main():
    a = Newclass(10, "Alex")
    b = Newclass(11, "Bob")

    print(a+b)



if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------

# python counter.py 1000 .5
# Heads: 483
# Tails: 517

# python counter.py 1000 .5
# Heads: 503
# Tails: 497

# python counter.py 1000 .3
# Heads: 280
# Tails: 720
