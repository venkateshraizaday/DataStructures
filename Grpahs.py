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
        for node in self.nodes.values():
            node.printDetails()

n = 5
edges = [(1,2),(2,3),(2,5),(4,5)]

g = Graph()
for i in range(n):
    g.nodes[i+1] = Node(i+1,[])
for (u,v) in edges:
    g.nodes[u].children.append(v)
    g.nodes[v].children.append(u)
g.printAll()