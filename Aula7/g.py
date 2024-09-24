def tic_tac_toe(arr):
    x = 0
    o = 0
    ganhou_o = False
    ganhou_x = False

    if 'X'.__eq__(arr[0][0]) and 'X'.__eq__(arr[1][1]) and 'X'.__eq__(arr[2][2]):
        ganhou_x = True
    elif 'O'.__eq__(arr[0][0]) and 'O'.__eq__(arr[1][1]) and 'O'.__eq__(arr[2][2]):
        ganhou_o = True
    
    if 'X'.__eq__(arr[0][2]) and 'X'.__eq__(arr[1][1]) and 'X'.__eq__(arr[2][0]):
        ganhou_x = True
    elif 'O'.__eq__(arr[0][2]) and 'O'.__eq__(arr[1][1]) and 'O'.__eq__(arr[2][0]):
        ganhou_o = True

    for line in range(3):
        if 'X'.__eq__(arr[line][0]) and 'X'.__eq__(arr[line][1]) and 'X'.__eq__(arr[line][2]):
            ganhou_x = True
        elif 'O'.__eq__(arr[line][0]) and 'O'.__eq__(arr[line][1]) and 'O'.__eq__(arr[line][2]):
            ganhou_o = True
        for column in range(3):
            if 'X'.__eq__(arr[0][column]) and 'X'.__eq__(arr[1][column]) and 'X'.__eq__(arr[2][column]):
                ganhou_x = True
            elif 'O'.__eq__(arr[0][column]) and 'O'.__eq__(arr[1][column]) and 'O'.__eq__(arr[2][column]):
                ganhou_o = True
            if 'X'.__eq__(arr[line][column]):
                x += 1
            elif 'O'.__eq__(arr[line][column]):
                o += 1
    
    if (ganhou_o and ganhou_x) or (x < o) or (x > o+1) or (ganhou_o and x > o) or (ganhou_x and o >= x):
        print('no')
        return
    print('yes')

inp = int(input())

for i in range(inp):
    arr = []
    for _ in range(3):
        arr.append(list(input()))

    tic_tac_toe(arr)
    try:
        input()
    except:
        pass