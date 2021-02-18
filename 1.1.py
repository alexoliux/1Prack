import math
from math import *

x, y = -41, -34
f1 = (exp(x) - pow(y, 4) - 28) / (82 * y - pow(x, 3))
f2 = sqrt(pow(x, 2) - 49 * pow(x, 3))
f3 = ((pow(x, 5)) / (13) + (x) / (93)) / (tan(y) - 67 * pow(y, 7))
f = f1 - f2 + f3
print("{:.2e}".format(f))
