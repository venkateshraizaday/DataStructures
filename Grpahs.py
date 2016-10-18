class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def printDetails(self):
        print(self.value, self.children)

class Graph:
    def __init__(self, nodes={}):
        self.nodes = nodes

    def printAll(self):
        for node in self.nodes:
            self.nodes[node].printDetails()

    def bfs(self,root):
        print("Bredth First Search:-")
        q = [root]
        visited = {}
        while len(q) != 0:
            node = q.pop(0)
            if node not in visited:
                print(node, end=' ')
                c = self.nodes[node].children
                visited[node] = True
                for child in c:
                    q.append(child)
        print()

    def dfs(self,root):
        print("Depth First Search:-")
        q = [root]
        visited = {}
        while len(q) != 0:
            node = q.pop()
            if node not in visited:
                print(node, end=' ')
                c = self.nodes[node].children
                visited[node] = True
                for child in c:
                    q.append(child)
        print()

n = 6
edges = [(0,5),(0,4),(0,1),(1,4),(1,3),(2,1),(3,2),(3,4)]

g = Graph()
for i in range(n):
    g.nodes[i] = Node(i,[])
for (u,v) in edges:
    g.nodes[u].children.append(v)
    #g.nodes[v].children.append(u)
g.printAll()
g.bfs(0)
g.dfs(0)