import math
from math import *


def f12(x):


    if x < 35:
        return exp(exp(x) - pow(x, 2)) - pow(x, 4) - 43

    elif 35 <= x < 68:
        return pow(x, 3) - 37 * x

    elif 68 <= x < 123:
        return 18 * pow(((pow(x, 3)) / (2) - (pow(x, 8)) / (60)), 8) - 65 * pow(x, 3)

    elif x >= 123:
        return pow((10 * pow(x, 6) + 84 * pow(x, 5)), 8) - exp(x)

print("{:.2e}".format(f12(-33)))
print("{:.2e}".format(f12(147)))
