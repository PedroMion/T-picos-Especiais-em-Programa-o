def verifyCounterfeit(inp):
    possibleLight = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])
    possibleHeavy = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])

    for i in range(3):
        arr = inp[i].split(" ")

        current = set(list(arr[0]) + list(arr[1]))
        if arr[2] == 'even':
            possibleLight -= current
            possibleHeavy -= current
        
        elif arr[2] == 'up':
            possibleLight = possibleLight.intersection(set(list(arr[1])))
            possibleHeavy = possibleHeavy.intersection(set(list(arr[0])))
        
        else:
            possibleLight = possibleLight.intersection(set(list(arr[0])))
            possibleHeavy = possibleHeavy.intersection(set(list(arr[1])))

    isLight = False
    response = (possibleLight.union(possibleHeavy)).pop()

    for i in range(3):
        arr = inp[i].split(" ")
        left = list(arr[0])
        
        if arr[2] != 'even':
            if response in left:
                if arr[2] == 'down':
                    isLight = True
            else:
                if arr[2] == 'up':
                    isLight = True

    print(f'{response} is the counterfeit coin and it is light.') if isLight == True else print(f'{response} is the counterfeit coin and it is heavy.')

qnt = int(input(""))

for i in range(qnt):
    arr = []
    arr.append(input(""))
    arr.append(input(""))
    arr.append(input(""))

    verifyCounterfeit(arr)
