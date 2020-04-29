def add_friends(nameOfPerson, listOfFriends):
    global friends
    if nameOfPerson not in friends:
        friends[nameOfPerson] = []
    friends[nameOfPerson].extend(listOfFriends)


def is_friends(nameOfPerson1, nameOfPerson2):
    if nameOfPerson2 in friends[nameOfPerson1]:
        return True
    else:
        return False


def print_friends(nameOfPerson):
     print(*sorted(friends[nameOfPerson]))

friends = {}
add_friends("Алла", ["Марина", "Иван"])
print(is_friends("Алла", "Марина"))
add_friends("Алла", ["Мария"])
print(is_friends("Алла", "Мария"))
print(friends)
print_friends("Алла")