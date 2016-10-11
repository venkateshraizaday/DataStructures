class Node:
    def __init__(self, children={}, count=0):
        self.children = children
        self.count = count

    def get(self, c):
        if c in self.children:
            return self.children[c]
        else:
            return None

    def insert(self, s):
        temp = self.children
        for c in s:
            if c in temp.children:
                temp = temp.children[c]
            else:
                node = Node()
                temp.children[c] = node
                temp.count += 1
                temp = temp.children[c]