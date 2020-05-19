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

# add
aa = Matrix([[1, 1],[1, 1],[1, 1]])
aa1 = Matrix([[2, 2],[2, 2],[2, 2]])
print(aa + aa1)
aa = Matrix([[1, 1],[1, 1],[1, 1]])
aa1 = Matrix([[2, 2],[2, 2],[2, 2]])
print(aa + aa1)



