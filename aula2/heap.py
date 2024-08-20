from heapq import heappush, heappop

def removeMin(heap, arr, numOperations):
    try:
        heappop(heap)
    except Exception:
        arr.append('insert 1')
        numOperations += 1
    arr.append('removeMin')
    numOperations += 1

    return numOperations, arr

def insert(heap, value, arr, numOperations):
    arr.append(f'insert {value}')
    numOperations += 1
    heappush(heap, value)

    return numOperations, arr

def getMin(heap, value, arr, numOperations):
    while True:
        try:
            minimum = heappop(heap)
            if minimum == value:
                arr.append(f'getMin {value}')
                numOperations += 1
                heappush(heap, value)
                return numOperations, arr
            elif minimum < value:
                arr.append('removeMin')
                numOperations += 1
            else:
                heappush(heap, minimum)
                insert(heap, value)
        except Exception:
            arr.append(f'insert {value}')
            arr.append(f'getMin {value}')
            heappush(heap, value)
            numOperations += 2
            return numOperations, arr

def heapOperations(list):    
    heap = []
    prints = []
    numOperations = 0
    for elem in list:
        if elem == 'removeMin':
            numOperations, prints = removeMin(heap, prints, numOperations)
        else:
            arr = elem.split(' ')

            if arr[0] == 'insert':
                numOperations, prints = insert(heap, int(arr[1]), prints, numOperations)
            else:
                numOperations, prints = getMin(heap, int(arr[1]), prints, numOperations)
    print(numOperations)
    for element in prints:
        print(element)

qnt = int(input(""))
arr = []

for i in range(qnt):
    arr.append(input(""))

heapOperations(arr)