def bracket_check(test_string):
    count = 0
    for bracket in test_string:
        if count >= 0:
            if bracket == "(" or bracket == "[" or bracket == "{":
                count += 1
            elif bracket == ")" or bracket == "]" or bracket == "}":
                count -= 1
        else:
            return print("NO")
    if count == 0:
        return print("YES")
    else:
        return print("NO")


bracket_check('{[((()]))}')