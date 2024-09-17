import sys

def ageSort(arr):
    count = [0] * 101
    for i in range(len(arr)):
        count[int(arr[i])] += 1
    
    resp = ""
    for i in range(len(count)):
        resp += f'{i} ' * count[i]
    
    print(resp.strip())


input = sys.stdin.read
data = input().split("\n")
size = 0
i = 0

while i < len(data):
    if data[i] == "0":
        break
    
    size = int(data[i])
    arr = []

    while len(arr) < size:
        i += 1
        arr += data[i].split(" ")

    i += 1
    ageSort(arr)