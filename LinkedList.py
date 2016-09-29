class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def Insert(self,value):
        node = Node(value)
        if(self.head is None):
            self.head = node
        else:
            ptr = self.head
            while(ptr.next != None):
                ptr = ptr.next
            ptr.next = node
        self.PrintAll()

    def RemoveLast(self):
        if(self.head.next == None):
            value = self.head.data
            self.head = None
            return value

        previousPtr = self.head
        ptr = self.head.next
        while(ptr.next != None):
            previousPtr = ptr
            ptr = ptr.next

        previousPtr.next = None
        return ptr.data

    def PrintAll(self):
        ptr = self.head
        print()
        while(ptr != None):
            print(ptr.data, end='')
            ptr = ptr.next

    def RemoveFirst(self):
        value = self.head.data
        self.head = self.head.next
        return value

    def RemoveValue(self,value):
        previousPtr = self.head
        ptr = self.head
        while(ptr is not None):
            if(ptr.data == value):
                previousPtr.next = ptr.next
            previousPtr = ptr
            ptr = ptr.next

linkedList = LinkedList()
linkedList.Insert(5)
linkedList.Insert(1)
linkedList.Insert(3)
linkedList.Insert(8)
linkedList.RemoveValue(3)
linkedList.PrintAll()