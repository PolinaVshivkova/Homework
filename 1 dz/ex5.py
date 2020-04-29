def eratosthenes(N):
    lst = [x for x in range(2, N + 1)]
    lst2 = []
    for i in lst:
        for j in lst:
            if j % i == 0 and j != i:
                lst2.append(j)
                lst.remove(j)
    print(*lst2)


eratosthenes(15)