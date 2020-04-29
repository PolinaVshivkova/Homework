from itertools import product

suit = ["пик", "треф", "бубен", "червей"]
value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

suit.remove(input())
for x, y in product(value,suit):
    print(x, y)