from matrix import Matrix

a = Matrix([[1, 1],[1, 1],[1, 1]])
a1 = Matrix([[2, 2],[2, 2],[2, 2]])
a2 = Matrix([[1, 1, 1],[1, 1, 1],[1, 1, 1]])
print(a.check_shape_for_add(a1), a.check_shape_for_add(a2))

b = Matrix([[1, 1],[1, 1],[1, 1]])
b1 = Matrix([[2, 2],[2, 2],[2, 2]])
b2 = Matrix([[1, 1, 1],[1, 1, 1]])
print(b.check_shape_for_mul(b1), a.check_shape_for_mul(b2))

c1 = Matrix([[2, 2],[2, 2],[2, 2]])
c = Matrix([[1, 1, 1],[1, 1, 1], [1, 1, 1]])
print(c.check_shape_square(), c1.check_shape_square())

# add, iadd
aa = Matrix([[1, 1],[1, 1],[1, 1]])
aa1 = Matrix([[2, 2],[2, 2],[2, 2]])
print(aa + aa1)
bb = Matrix([[2, 1],[2, 1],[2, 1]])
bb1 = Matrix([[3, 2],[3, 2],[3, 2]])
print(bb + bb1)
aa += aa1
bb += bb1
print(aa, bb)

# sub, isub
cc = Matrix([[4, 4],[4, 4],[4, 4]])
cc1 = Matrix([[2, 1],[3, 1],[2, 3]])
print(cc - cc1)
dd = Matrix([[5, 5],[5, 5],[5, 5]])
dd1 = Matrix([[1, 1],[1, 1],[1, 1]])
print(dd - dd1)
cc -= cc1
dd -= dd1
print(cc, dd)

# mul, imul
cd = Matrix([[2, 3],[2, 3]])
cd1 = Matrix([[2, 1],[3, 1]])
print(cd * cd1)
dc = Matrix([[1, 2, 3],[3, 4, 5],[5, 6, 7]])
dc1 = 2
print(dc * dc1)
cd *= cd1
dc *= dc1
print(cd, dc)

# repr
print(repr(cd))
print(repr(dc))

# setitem, getitem
print(dc[1][1])

# determinant
e = Matrix([[5, -2], [4, 3]])
e1 = Matrix([[2, 3, 4], [5, 1, -3], [-3, -2, 1]])
print(e.determinant(), e1.determinant())

#  is_degenerate
e = Matrix([[2, 4], [3, 6]])
e1 = Matrix([[5, 4, -6], [1, 3, 0], [4, 7, -4]])
print(e.is_degenerate(), e1.is_degenerate())

# kramer_solution
f = Matrix([[2, -1, 3], [4, 3, -1], [1, -2, 5]])
f1 = Matrix([[2, 5, -3], [3, -2, 1], [7, 4, -5]])
ff = [13, 7, 15]
ff1 =[-15, 20, -6]
print(f.kramer_solution(ff), f1.kramer_solution(ff1))

# gauss_solution
print(f.gauss_solution(ff), f1.gauss_solution(ff1))

# inverse
print(f.inverse(), f1.inverse())

# проверка на время
x1 = Matrix(2, 2)
x2 = Matrix(5, 5)
x3 = Matrix(10, 10)
x4 = Matrix(20, 20)
y1 = Matrix(1, 2)
y2 = Matrix(1, 5)
y3 = Matrix(1, 10)
y4 = Matrix(1, 20)
print(x1.kramer_solution(*y1), x1.gauss_solution(*y1), sep="\n")
print(x2.kramer_solution(*y2), x2.gauss_solution(*y2), sep="\n")
print(x3.kramer_solution(*y3), x3.gauss_solution(*y3), sep="\n")
print(x4.kramer_solution(*y4), x4.gauss_solution(*y4), sep="\n")