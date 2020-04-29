def find_farthest_orbit(list_of_orbits):
    lst_ar = list(map(lambda x: x[0] * x[1], list(filter(lambda x: x[0] != x[1], list_of_orbits))))
    ar, orbit = 0, 0
    for i in range(len(lst_ar)):
        if ar < lst_ar[i]:
            ar, orbit = lst_ar[i], list_of_orbits[i]
    return orbit




orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))