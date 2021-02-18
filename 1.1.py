import math
from math import *


def f11(x, y):
    return (exp(x) - pow(y, 4) - 28) / (82 * y - pow(x, 3)) - (sqrt(pow(x, 2) - 49 * pow(x, 3))) + (
                ((pow(x, 5)) / (13) + (x) / (93)) / (tan(y) - 67 * pow(y, 7)))


print("{:.2e}".format(f11(-41, -34)))
print("{:.2e}".format(f11(-3, -32)))
