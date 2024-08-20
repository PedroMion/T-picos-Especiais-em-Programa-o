def transformWord(word):
    word = word.lower()

    arr = list(word)
    arr.sort()

    return "".join(arr)

def countAnanagram(arr, dict):
    response = []
    
    for word in arr:
        if dict[transformWord(word)] == 1:
            response.append(word)
    
    return response

def createMap(words):
    dict = {}

    for word in words:
        if word == "":
            continue
        treated = transformWord(word)

        if treated in dict:
            dict[treated] += 1
        else:
            dict[treated] = 1
    
    return dict

def printAnanagrams(words):
    dict = createMap(words)
    response = countAnanagram(words, dict)
    response.sort()

    for ananagram in response:
        print(ananagram)

arr = []
while True:
    inp = input("")

    if inp == '#':
        printAnanagrams(arr)
        break
    else:
        words = inp.split(" ")

        for elem in words:
            arr.append(elem)