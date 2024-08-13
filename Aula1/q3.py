def subString(input):
    dict = {}
    result = 0
    i = 0

    for letter in input:
        if letter in dict:
            result += 2
            dict = {}
        else:
            dict[letter] = i
        i += 1
    
    return len(input) - result

size = int(input(""))

for _ in range(size):
     val = input("")
     print(subString(val))