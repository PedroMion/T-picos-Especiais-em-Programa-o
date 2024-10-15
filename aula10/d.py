def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, x, y):
    xset = find(parent, x)
    yset = find(parent, y)
    if xset != yset:
        if xset > yset:
            parent[yset] = xset
        else:
            parent[xset] = yset

def friends(n, edges):
    parent = []

    for i in range(n):
        parent.append(i)
    
    for edge in edges:
        union(parent, edge[0], edge[1])
    
    for i in range(n):
        find(parent, i)

    return parent.count(max(set(parent), key=parent.count))

qntTestes = int(input())

for _ in range(qntTestes):
    n_m_line = input().split(" ")
    n = int(n_m_line[0])
    m = int(n_m_line[1])
    arr = []

    for _ in range(m):
        temp = input().split(" ")

        arr.append([int(temp[0]) -1, int(temp[1]) - 1])
    
    print(friends(n, arr))
