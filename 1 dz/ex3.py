def squared():
    for ten in range(1, 10):
        for unit in range(1,10):
            square = (ten * 10 + unit) ** 2
            if unit == 9:
                print(square, end="\n")
            else:
                if square > 1000:
                    print(square, end='  ')
                else:
                    print(square, end='   ')



squared()
