import math
from math import *


def f14(n):
    if n == 0:
        return 3
    else:
        return (1) / (8) * f(n - 1) + tan(f(n - 1))


print("{:.2e}".format(f14(15)))
print('%.2e' % f14(10))