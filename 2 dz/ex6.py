def transpose(matrix):
    matrix[:] = list(zip(*matrix))


matrix = [[1, 2], [3, 4], [5, 6]]
transpose(matrix)
for line in matrix:
    print(*line)