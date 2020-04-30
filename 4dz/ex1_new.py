import sys

lst = []
d = dict()
for line in sys.stdin:
    lst.append(list(line.split()))
for country in lst:
    count = int(country[2]) // 100000 * 100
    d[count] = d.get(count, []) + [country[0]]
d = sorted(d.items())
for count, capital in d:
    print(f"{count} - {int(count) + 100}: ", end=" ")
    print(*sorted(capital), sep=", ")
