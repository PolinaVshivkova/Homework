def fractal_print(obj):
    fractal_1 = []
    fractal_1.extend(obj)
    print(fractal_1)

fractal = [3]
fractal.append(fractal)
fractal.append(2)  # [3, [...], 2]
fractal_print(fractal)
