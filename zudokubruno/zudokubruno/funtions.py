import random

def swap_row(mapa):
    row = random.randint(0,8)
    rest = row%3
    n = row//3
    if rest == 0:
        swap_rest = 1
    else:
        swap_rest = 0
    swaped_row = mapa[row].copy()
    mapa[row] = mapa[n*3+swap_rest]
    mapa[n*3+swap_rest] = swaped_row

    return mapa

def swap_numbers(mapa):
    num1 = random.randint(5,9)
    num2 = random.randint(1,4)
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == num1:
                mapa[i][j] = num2
            elif mapa[i][j] == num2:
                mapa[i][j] = num1
    return mapa
