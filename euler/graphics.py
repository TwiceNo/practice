from numpy import linspace as ls
from math import sqrt, e, log


class Accurate:
    dots = {}

    def __init__(self, n = 1000):
        self.dots = {}
        x = ls(1, 2, n + 1)
        for xi in x:
            self.dots[xi] = self.func(xi)

    def func(self, val):
        return val ** 4 * log(val * e) ** 2


class Approach:
    dots = {}
    n, h = 1, 1

    def __init__(self, n):
        self.dots = {}
        self.h, self.n = 1 / n, n
        self.calculate()

    def func(self, x, y):
        return (4 * y + 2 * x ** 2 * sqrt(y)) / x

    def euler(self, x, y):
        return y + self.h * self.func(x, y)

    def calculate(self):
        x, y = ls(1, 2, self.n + 1), [1]
        for i in range(self.n + 1):
            y.append(self.euler(x[i], y[i]))
            self.dots[x[i]] = y[i]

