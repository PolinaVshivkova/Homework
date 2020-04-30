from math import gcd
from functools import reduce
import sys

lst = []
for line in sys.stdin:
    lst.append(int(line.rstrip()))
print(reduce(gcd, lst))