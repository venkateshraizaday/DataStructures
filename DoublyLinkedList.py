class Node:
    def __init__(self,data, previous= None, next = None):
        self.data = data
        self.previous = previous
        self.next = next

class DoublyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def PrintAll(self):
        ptr = self.head
        while(ptr is not None):
            print(ptr.data, end='')
            ptr = ptr.next
        print()

    def Insert(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            ptr = self.head
            while(ptr.next is not None):
                ptr = ptr.next
            ptr.next = node
            node.previous = ptr
        self.PrintAll()

    def Delete(self,value):
        ptr = self.head
        while(ptr is not None):
            if(ptr.data == value):
                tempPtr = ptr.previous
                tempPtr.next = ptr.next
                return ptr.data
            else:
                ptr = ptr.next

dll = DoublyLinkedList()
dll.Insert(1)
dll.Insert(2)
dll.Insert(3)
dll.Insert(4)
print("Value deleted: "+str(dll.Delete(3)))
dll.PrintAll()