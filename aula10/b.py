def minimunHeight(arr):
    if len(arr) < 2:
        return 0
    
    lines = [[arr[0]], []]
    currentLine = 1
    currentNode = 0

    i = 1

    while i < len(arr):
        if currentNode == len(lines[currentLine-1]):
            currentLine += 1
            currentNode = 0
            lines.append([arr[i]])
            i += 1
        else:
            lines[currentLine].append(arr[i])
            i += 1

        while i < len(arr) and arr[i] > arr[i-1]:
            lines[currentLine].append(arr[i])
            i += 1

        currentNode += 1
    
    return len(lines) - 1

qntTestes = int(input())

for _ in range(qntTestes):
    n = int(input())
    order = input().split(" ")
    arr = []

    for elem in order:
        if elem != "":
            arr.append(int(elem))
    
    print(minimunHeight(arr))