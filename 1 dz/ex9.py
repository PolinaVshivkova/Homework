def password_level(password):
    le = len(password)
    if le < 6:
        return ("Недопустимый пароль")
    else:
        count_num = len(list(filter(lambda x: x.isdigit(), password)))
        count_2 = len(list(filter(lambda x: x.isdigit, password)))
        count_3 = len(list(filter(lambda x: x.isdigit, password)))
        if le == count_lower or le == count_upper or le == count_num:
            return ("Ненадежный пароль")
        elif le == count_num + count_lower or le == count_num + count_upper or le == count_upper + count_lower:
            return ("Cлабый пароль")
        else:
            return ("Надежный пароль")


print(password_level("ghs"))
print(password_level("ывапПРОро"))
print(password_level("1478SDFGHJK4fghjkl56"))