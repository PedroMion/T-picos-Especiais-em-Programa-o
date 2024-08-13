def calculateCandidate(list):
    maxValue = max(list)
    result = ""

    quant = 0

    for elem in list:
        if elem == maxValue:
            quant += 1

    for i in range(3):
        if maxValue == list[i] and quant == 1:
            result += str(maxValue - list[i]) + " "
        else:
            result += str(maxValue - list[i] + 1) + " "
    print(result)

qntInput = int(input(""))

for i in range(qntInput):
    votes = input("")
    arrVotes = [int(elem) for elem in votes.split(" ")]

    calculateCandidate(arrVotes)