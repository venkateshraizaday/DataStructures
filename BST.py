class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self,root=None):
        self.root = root

    def Insert(self,value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
        else:
            ptr = self.root
            while True:
                if newNode.data > ptr.data:
                    if ptr.right is None:
                        ptr.right = newNode
                        break
                    else:
                        ptr = ptr.right
                else:
                    if ptr.left is None:
                        ptr.left = newNode
                        break
                    else:
                        ptr = ptr.left

    def Traverse(self,node):
        if node is None:
            return
        self.Traverse(node.left)
        print(node.data, end=' ')
        self.Traverse(node.right)


bst = BinarySearchTree()
for e in [5,2,8,4,2,7,6,8]:
    bst.Insert(e)
bst.Traverse(bst.root)