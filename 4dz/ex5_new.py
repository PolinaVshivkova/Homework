import sys

lst, lst_1 = [], []
for line in sys.stdin:
    lst.append(line.split())
lst = list(filter(lambda x: x != [], lst))
for i in lst:
    lst_1.append(list(map(int, i)))

if all([sum(x) == sum(lst_1[0]) for x in lst_1]) and all([sum(y) == sum(lst_1[0]) for y in list(zip(*lst_1))]):
    print("YES")
else:
    print("NO")
