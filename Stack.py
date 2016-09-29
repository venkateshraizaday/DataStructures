class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, head=None):
        self.head = head

    def IsEmpty(self):
        return self.head is None

    def Push(self, d):
        node = Node(d)
        node.next = self.head
        self.head = node

    def Pop(self):
        if(not self.IsEmpty()):
            temp = self.head.data
            self.head = self.head.next
        else:
            temp = "Stack is empty."
        return temp

    def Peek(self):
        if(not self.IsEmpty()):
            return self.head.data
        return "Stack is empty"



stack = Stack()
stack.Push(1)
stack.Push(2)
temp = stack.Pop()
print(temp)
temp = stack.Peek()
print(temp)
temp = stack.Pop()
print(temp)
temp = stack.Peek()
print(temp)
temp = stack.Pop()
print(temp)