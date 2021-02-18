import math
from math import *

x = -33
if int(x < 35):
    f1 = exp(exp(x) - pow(x, 2)) - pow(x, 4) - 43
    print("{:.2e}".format(f1))
elif 35 <= x < 68:
    f2 = pow(x, 3) - 37 * x
    print("{:.2e}".format(f2))
elif 68 <= x < 123:
    f3 = 18 * pow(((pow(x, 3)) / (2) - (pow(x, 8)) / (60)), 8) - 65 * pow(x, 3)
    print("{:.2e}".format(f3))
elif x >= 123:
    f4 = pow((10 * pow(x, 6) + 84 * pow(x, 5)), 8) - exp(x)
    print("{:.2e}".format(f4))
