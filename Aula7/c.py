def domino(left, right, gap, pieces):
    match = left[2]

    if gap == 1:
        for elem in pieces:
            if (elem[0] == left[2] and elem[2] == right[0]) or (elem[2] == left[2] and elem[0] == right[0]):
                return "YES"
        return "NO"
    
    for i in range(len(pieces)):
        if match == pieces[i][0]:
            temp = pieces[:]
            temp.remove(pieces[i])
            
            resp = domino(pieces[i], right, gap-1, temp)
            if resp == "YES":
                return resp
    
    for i in range(len(pieces)):
        if match == pieces[i][2]:
            temp = pieces[:]
            temp.remove(pieces[i])
        
            resp = domino(f'{pieces[i][2]} {pieces[i][0]}', right, gap-1, temp)
            if resp == "YES":
                return resp
    
    return "NO"

try:
    while True:
        n = int(input())

        if n == 0:
            break

        m = int(input())
        left = input()
        right = input()
        arr = []
        
        for _ in range(m):
            arr.append(input())
    
        print(domino(left, right, n, arr))
except:
    pass