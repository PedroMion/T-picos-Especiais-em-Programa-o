def minority(input):
    qntZero = 0
    qntOne = 0

    for letter in input:
        if letter == '1':
            qntOne += 1
        else:
            qntZero += 1
    
    if qntZero == qntOne:
        print(qntZero - 1)
    else:
        print(min(qntZero, qntOne))

qntInput = int(input("")) #0101010101010011

for i in range(qntInput):
    binaryString = input("")

    minority(binaryString)