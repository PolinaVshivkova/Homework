def mean(arr):
    return 0 if not arr else sum(arr) / len(arr)


def median(arr):
    num = len(arr) // 2
    if len(arr) % 2 != 0:
        return sorted(arr)[num]
    else:
        return (sorted(arr)[num] + sorted(arr)[num - 1]) / 2


def print_statistics(arr):
    if arr:
        print(len(arr))
        print(mean(arr))
        print(min(arr))
        print(max(arr))
        print(median(arr))
    else:
        print(0)
    print()


print_statistics([])
print_statistics([22])
print_statistics([3,5,8,4])