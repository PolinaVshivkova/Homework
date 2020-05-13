import sys

lst = []
for line in sys.stdin:
    lst.append(line.lstrip("#"))
    lst1 = []
    for i in range(len(lst)):
        lst1.append(f'Line {i + 1}: {lst[i][1:-2:]}')

print(*lst1, sep="\n")