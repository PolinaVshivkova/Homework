letter = {"A": 1, "B": 2, "C" :3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8 }
number = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}


def possible_turns(cell):
    coor = []
    cell_start = in_numbers(cell)
    coor.append([cell_start[0] - 2, cell_start[1] - 1])
    coor.append([cell_start[0] - 2, cell_start[1] + 1])
    coor.append([cell_start[0] + 2, cell_start[1] - 1])
    coor.append([cell_start[0] + 2, cell_start[1] + 1])
    coor.append([cell_start[0] - 1, cell_start[1] - 2])
    coor.append([cell_start[0] - 1, cell_start[1] + 2])
    coor.append([cell_start[0] + 1, cell_start[1] - 2])
    coor.append([cell_start[0] + 1, cell_start[1] + 2])
    newcoor = sorted(check(coor))
    return newcoor


def in_numbers(cell):
    n1 = letter[cell[0]]
    n2 = int(cell[1])
    return tuple([n1, n2])


def check(lst_cell):
    new_lst = []
    for cell in lst_cell:
        n1, n2 = cell[0], cell[1]
        if 8 > cell[0] > 0 and 8 > cell[1] > 0:
            new_lst.append(in_letters(cell))
    return new_lst


def in_letters(cell):
    n1 = number[cell[0]]
    n2 = str(cell[1])
    return str(n1 + n2)


print(possible_turns("B1"))
print(possible_turns("H8"))
