import math

def maxGcd(arr):
    maxi = 1

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            gcd = math.gcd(int(arr[i]), int(arr[j]))

            if gcd > maxi:
                maxi = gcd
    
    print(maxi)

qnt = int(input())

for i in range(qnt):
    ent = input().split(" ")
    arr = []

    for elem in ent:
        if elem != '':
            arr.append(elem)

    maxGcd(arr)
    