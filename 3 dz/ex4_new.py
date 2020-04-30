import sys

words = []
for line in sys.stdin:
    words.append(line.rstrip())
lst = sorted(words, key=lambda x: sum(ord(i) - ord("A") + 1 for i in x.upper()))

print(*lst, sep="\n")