def swap(elem):
    if elem == '#':
        return 'O'
    return '#'

def switch(board, i, j):
    board[i][j] = swap(board[i][j])
    if i > 0:
        board[i-1][j] = swap(board[i-1][j])
    if i < 9:
        board[i+1][j] = swap(board[i+1][j])
    if j > 0:
        board[i][j-1] = swap(board[i][j-1])
    if j < 9:
        board[i][j+1] = swap(board[i][j+1])

def lightSwitch(board, name):
    response = []
    
    for counter in range(1024):
        s = f'{counter:010b}'
        buttonsPushed = 0
        temp = board[:]

        for i in range(10):
            if s[i] == '1':
                buttonsPushed += 1
                switch(temp, 0, i)
        
        for j in range(1, 10):
            line = temp[j-1]
            for k in range(len(line)):
                if line[k] == 'O':
                    buttonsPushed += 1
                    switch(temp, j, k)
        
        isWin = True
        for char in temp[9]:
            if char == 'O':
                isWin = False
                break
        if isWin:
            response.append(buttonsPushed)
    
    if len(response) == 0:
        print(f'{name} 0')

    response.sort()
    print(f'{name} {response[0]}')

inp = input()

while input != "end":
    arr = []
    for _ in range(10):
        arr.append(list(input()))
    
    lightSwitch(arr, inp)
    inp = input()