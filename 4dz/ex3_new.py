import sys
from functools import reduce

lst = list(map(str.rstrip, sys.stdin))

print(reduce(lambda x, y: x if x < y else y, lst))