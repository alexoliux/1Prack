import math
from math import *


def f13(n, m):
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += exp(i) - pow(i, 4) - 28
    sum2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sum2 += 18 * pow(i, 7) - sin(j)
    return sum1 + sum2


print('%.2e' % f13(22, 47))
print('%.2e' % f13(32, 33))
