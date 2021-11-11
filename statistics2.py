import math
"""
Statistics. Develop a data type for maintaining statistics in a set of floats.
Provide a method to add data points and methods that return the number of points,
the mean, the standard deviation, and the variance. Develop two implementations:
one whose instance values are the number of points, the sum of the values, and
the sum of the squares of the values, and another that keeps an array containing
all the points. For simplicity, you may take the maximum number of points in the
constructor. Your first implementation is likely to be faster and use substantially
less space, but is also likely to be susceptible to round-off error. See the booksite for
a well-engineered alternative. 
"""

class Statistics:
    def __init__(self, trials):
        self.l = trials[:]
        self.length = len(trials)
        self.sum = sum(trials)


    def __str__(self):
        return "Sample size: " + str(self.length) + '\nSample values: ' + str(self.l)

    def sample_size(self):
        return self.length

    def mean(self):
        return self.sum / self.length

    def add_point(self, point):
        self.l += point

    def variance(self):
        mean = self.mean()
        t = self.l
        n = self.length
        sum = 0
        for i in range(self.length):
            sum += pow(t[i] - mean, 2)
        return sum / (n - 1)

    def stddev(self):
        return math.sqrt(self.variance())


def main():
    trials = [0.1, 0.2, 0.3, 1.1, 1.2, 0.5, 0.4, 1.11, 2.11, 3, 2]
    sample = Statistics(trials)
    print(sample)
    print('Sample size:', sample.sample_size())
    print('Variance: ' + str(sample.variance()))
    print('Standard deviation:', str(sample.stddev()))


if __name__ == '__main__':
    main()
