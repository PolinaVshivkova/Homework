def solve(*coefficients):
    if len(coefficients) > 3 or not coefficients:
        return None
    elif len(coefficients) == 3:
        a, b, c = [*coefficients]
        d = b ** 2 - 4 * a * c
        return (- b + d ** (0.5)) / (2 * a), (- b - d ** (0.5)) / (2 * a)
    elif len(coefficients) == 2:
        b, c = [*coefficients]
        return -c / b
    else:
        return "Нет корней"


print(sorted(solve(1, -3, 2)))