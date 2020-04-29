def choose_coffee(preferences):
    coffee_dict = {"Эспрессо": [1, 0, 0],  # 0 - кофейные зерна, 1 - молоко, 2 - взбитые сливки
                   "Капучино": [1, 3, 0],
                   "Маккиато": [2, 1, 0],
                   "Кофе по-венски": [1, 0, 2],
                   "Латте Маккиато": [1, 2, 1],
                   "Кон Панна": [1, 0, 1]}
    for i in preferences:
        if ingredients[0] != 0 and ingredients[1] - coffee_dict[i][1] >= 0 and ingredients[2] - coffee_dict[i][2] >= 0:
            ingredients[0] -= coffee_dict[i][0]
            ingredients[1] -= coffee_dict[i][1]
            ingredients[2] -= coffee_dict[i][2]
            return i
    return "К сожалению, не можем предложить Вам напиток"


ingredients = [4, 4, 0]
print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))
print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))
print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))
print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))