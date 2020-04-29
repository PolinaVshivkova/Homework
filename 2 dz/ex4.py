def swap(first, second):
    copy_2, copy_1 = second.copy(), first.copy()
    first.clear()
    second.clear()
    for x in copy_2:
        first.append(x)
    for x in copy_1:
        second.append(x)


first = [1, 2, 3]
second = [4, 5, 6]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)