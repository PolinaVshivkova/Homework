def polite_input(question):
    global name
    if not name:
        name = input("Как вас зовут? ")
    return f'{name}, {question}'


name = 0
age = polite_input('укажите возраст')
school_number = polite_input('укажите номер школы')
class_num = polite_input('укажите полный номер класса')