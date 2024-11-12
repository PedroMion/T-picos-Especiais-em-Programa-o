def dfs(node, graph, visited):
    visited[node] = 1

    for elem in graph[node]:
        if visited[elem] == 0:
            dfs(elem, graph, visited)


def morning_walk(V, E):
    degrees = [0] * V
    graph = [[] for _ in range(V)]
    visited = [1] * V

    if E == 0:
        print("Not Possible")
        return

    for _ in range(E):
        u, v = map(int, input().split())
        degrees[u] += 1
        degrees[v] += 1
        graph[u].append(v)
        graph[v].append(u)
        visited[u] = 0
        visited[v] = 0

    for i in range(V):
        if degrees[i] % 2 == 1:
            print("Not Possible")
            return

    resp = False
    for i in range(V):
        if visited[i] == 0:
            dfs(i, graph, visited)

            for elem in visited:
                if elem == 0:
                    print("Not Possible")
                    return
            
            print("Possible")
            return

while True:
    try:
        inp = input().split(" ")

        if inp[0] == '':
            continue

        V = int(inp[0])
        E = int(inp[1])

        morning_walk(V, E)
    except EOFError:
        break