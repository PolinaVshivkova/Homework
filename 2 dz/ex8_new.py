import random

scoring = {"Яблочко": 50,
           "Зеленое кольцо": 25,
           "Внешнее кольцо": [random.randint(0, 50) for x in range(20)],
           "Внутренне кольцо": [random.randint(0, 50) for x in range(20)]}


def score(ring, sector=0):
    if sector:
        return scoring[ring][sector]
    else:
        return scoring[ring]


print(score("Внешнее кольцо", 1))
print(score("Яблочко"))