class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def PrintAll(self):
        ptr = self.head
        while(ptr is not None):
            print(ptr.data, end=' ')
            ptr = ptr.next
        print()

    def Enqueue(self,value):
        node = Node(value)
        if(self.head is None):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.PrintAll()

    def Dequeue(self):
        if(self.head is None):
            return "Queue is empty"
        value = self.head.data
        self.head = self.head.next
        if(self.head is None):
            self.tail = None
        return value

queue = Queue()
queue.Enqueue(1)
queue.Enqueue(2)
print(queue.Dequeue())
print(queue.Dequeue())
print(queue.Dequeue())