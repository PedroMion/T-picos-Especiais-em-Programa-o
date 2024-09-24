def swap(s, i, j):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)

def recursion(s, index, arr):
    if s == s[0] * (len(s) - index):
        arr.append(s)
        return
    if index == len(s) - 1:
        arr.append(s)
        return
    
    for i in range(index, len(s)):
        s = swap(s, index, i)
        recursion(s, index + 1, arr)
        s = swap(s, index, i)

def permute(s):
    arr = []
    recursion(s, 0, arr)
    return arr

n = int(input())

for _ in range(n):
    s = input()
    s = list(s)
    s.sort()
    s = "".join(s)

    arr = permute(s)
    dic = {}
    arr.sort()

    for elem in arr:
        if elem not in dic.keys():
            print(elem)
            dic[elem] = 1
    
    print("")