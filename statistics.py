import math


class Statistics:
    def __init__(self, trials):
        self.l = trials[:]
        self.length = len(trials)

    def __str__(self):
        return "Sample size: " + str(self.length) + '\nSample values: ' + str(self.l)

    def sample_size(self):
        return self.length

    def mean(self):
        sum = 0
        t = self.l
        for i in range(self.length):
            sum += t[i]
        return sum / self.length

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
    print("Sample size: " + str(sample.sample_size()))
    print("Variance: " + str(sample.variance()))
    print("Standard deviation: " + str(sample.stddev()))


if __name__ == '__main__':
    main()
