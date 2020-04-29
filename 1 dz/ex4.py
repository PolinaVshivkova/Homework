def tic_tac_toe(field):
    if field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]:
        print("win ", field[1][1])
        return
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2]:
            print("win ", field[i][2])
            return
        if field[0][i] == field[1][i] == field[2][i]:
            print("win ", field[2][i])
            return
    print("draw")


data = """x 0 x
0 0 0
0 - x"""
field = [line.split() for line in data.split('\n')]
tic_tac_toe(field)