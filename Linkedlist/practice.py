class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None

    def addElementInBeginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printList(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def addElementInLast(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = node


    def search(self, target):
        current =  self.head
        while current:
            if current.data == target:
                print("Yes found")
                break
            current = current.next

    def deleteFirst(self):
        if self.head is None:
            return None
        self.head = self.head.next

    def deleteLast(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.deleteFirst()
            return
        
        current = self.head
        while current.next.next:
            current = current.next

        current.next = None

    def deleteByValue(self, value):
        if self.head is None:
            return 
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        current = self.head

        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next


    

obj = Linklist()
obj.addElementInBeginning(1)
obj.addElementInLast(2)
obj.addElementInLast(3)
obj.addElementInLast(4)
obj.addElementInLast(5)
obj.printList()
obj.deleteByValue(4)
obj.printList()