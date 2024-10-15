class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [ [] for _ in range(n) ]
        self.degrees = [0] * n
    
    def add_edge(self, m, n):
        self.edges[m].append(n)
        self.edges[n].append(m)
        self.degrees[n] += 1
        self.degrees[m] += 1
    
    def remove_node(self, node):
        self.degrees[node] = -1

        for i in range(len(self.edges)):
            if i == node:
                self.edges[i] = []
            elif node in self.edges[i]:
                self.edges[i].remove(node)
                self.degrees[i] = -1
    
    def get_highest_degree_node(self):        
        max = -1
        resp = -1

        for i in range(len(self.degrees)):
            if self.degrees[i] > max:
                resp = i
        
        return resp

    def count_edges(self):
        counter = 0
        
        for elem in self.edges:
            counter += len(elem)
        
        return counter

def countGuards(graph):
    count = 0
    maxDegree = graph.get_highest_degree_node()

    while maxDegree != -1:
        graph.remove_node(maxDegree)
        count += 1

        maxDegree = graph.get_highest_degree_node()
    
    if graph.count_edges() > 0:
        return -1
    return count

qntTestes = int(input())

for _ in range(qntTestes):
    n_m_line = input().split(" ")
    n = int(n_m_line[0])
    m = int(n_m_line[1])
    arr = []
    graph = Graph(n)

    for _ in range(m):
        temp = input().split(" ")

        graph.add_edge((int(temp[0])), (int(temp[1])))
    
    print(countGuards(graph))
