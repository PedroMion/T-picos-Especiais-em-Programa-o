import bisect, math

def getMedian(arr):
    size = len(arr)
    if size == 1:
        return arr[0]
    elif size % 2 != 0:
        return arr[(size-1) // 2]
    else:
        return math.floor((arr[size // 2] + arr[(size // 2) - 1]) / 2)

arr = []
try:
    while True:
        inp = int(input().strip())
        bisect.insort(arr, inp)
        print(getMedian(arr))
except:
    pass