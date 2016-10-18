class Node:
    def __init__(self, data, height=1, left=None, right=None):
        self.data = data
        self.height = height
        self.left = left
        self.right = right

class AVLTree:
    def __init__(self, root=None):
        self.root = root

    def GetHeight(self,node):
        if node is None:
            return 0
        return node.height

    def GetBalanceFactor(self,node):
        if node is None:
            return 0
        else:
            return self.GetHeight(node.left) - self.GetHeight(node.right)

    def RightRotation(self,node):
        n1 = node.left
        t = n1.right
        n1.right = node
        node.left = t

        node.height = max(self.GetHeight(node.left),self.GetHeight(node.right)) + 1
        n1.height = max(self.GetHeight(n1.left), self.GetHeight(n1.right)) + 1

        return n1

    def LeftRotation(self, node):
        n1 = node.right
        t = n1.left
        n1.left = node
        node.right = t

        node.height = max(self.GetHeight(node.left), self.GetHeight(node.right)) + 1
        n1.height = max(self.GetHeight(n1.left), self.GetHeight(n1.right)) + 1

        return n1

    def Insert(self,node,value):
        if node is None:
            return Node(value)

        if node.data > value:
            node.left = self.Insert(node.left,value)
        else:
            node.right = self.Insert(node.right,value)

        node.height = max(self.GetHeight(node.left), self.GetHeight(node.right)) + 1
        bf = self.GetBalanceFactor(node)

        if bf > 1 and value < node.left.data:
            return self.RightRotation(node)

        if bf < -1 and value > node.right.data:
            return self.LeftRotation(node)

        if bf > 1 and value > node.left.data:
            node.left = self.LeftRotation(node.left)
            return self.RightRotation(node)

        if bf < -1 and value < node.right.data:
            node.right = self.RightRotation(node.right)
            return self.LeftRotation(node)

        return node

    def InOrderTraversal(self,node):
        if node is None:
            return
        self.InOrderTraversal(node.left)
        print(node.data, self.GetBalanceFactor(node))
        self.InOrderTraversal(node.right)

    def PreOrderTraversal(self,node):
        if node is None:
            return
        print(node.data, self.GetBalanceFactor(node))
        self.InOrderTraversal(node.left)
        self.InOrderTraversal(node.right)

avlTree = AVLTree()
avlTree.root = avlTree.Insert(avlTree.root,1)
avlTree.root = avlTree.Insert(avlTree.root,3)
avlTree.root = avlTree.Insert(avlTree.root,6)
avlTree.root = avlTree.Insert(avlTree.root,10)
avlTree.root = avlTree.Insert(avlTree.root,15)
avlTree.root = avlTree.Insert(avlTree.root,21)
avlTree.root = avlTree.Insert(avlTree.root,28)
avlTree.root = avlTree.Insert(avlTree.root,36)
avlTree.root = avlTree.Insert(avlTree.root,45)
avlTree.root = avlTree.Insert(avlTree.root,55)
avlTree.root = avlTree.Insert(avlTree.root,66)
print("Tree traversal")
avlTree.InOrderTraversal(avlTree.root)
avlTree.PreOrderTraversal(avlTree.root)