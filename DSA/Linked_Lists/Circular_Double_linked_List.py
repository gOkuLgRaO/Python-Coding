class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def create(self, value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        newnode.prev = newnode
        newnode.next = newnode
        return "The CDLL is created"

    def insert(self, value, location):
        newnode = Node(value)
        if self.head is None:
            return "Head does not exist"
        else:
            if location == 0:
                newnode.next = self.head
                newnode.prev = self.tail
                self.head.prev = newnode
                self.head = newnode
                self.tail.next = newnode

            elif location == 1:
                newnode.next = self.head
                newnode.prev = self.tail
                self.head.prev = newnode
                self.tail.next = newnode
                self.tail = newnode

            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                newnode.next = tempnode.next
                newnode.prev = tempnode
                newnode.next.prev = newnode
                tempnode.next = newnode

    def traverse(self):
        if self.head is None:
            return "Head is none"
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                if tempnode == self.tail:
                    break
                tempnode = tempnode.next

    def reverse_traverse(self):
        if self.head is None:
            return "Head is none"
        else:
            tempnode = self.tail
            while tempnode:
                print(tempnode.value)
                if tempnode == self.head:
                    break
                tempnode = tempnode.prev

    def search(self, value):
        if self.head is None:
            return "There is no head"
        tempnode = self.head
        while tempnode:
            if tempnode.value == value:
                return tempnode.value
            if tempnode == self.tail:
                return "The values does not exist"
            tempnode = tempnode.next

    def delete(self, location):
        if self.head is None:
            return "Head does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head

            elif location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail

            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                tempnode.next = tempnode.next.next
                tempnode.next.prev = tempnode
            print("Node successfully deleted")

    def delete_entirely(self):
        if self.head is None:
            return "There is no head"
        else:
            self.tail.next = None
            tempnode = self.head
            while tempnode:
                tempnode.prev = None
                tempnode = tempnode.next
            self.head = None
            self.tail = None
            print("CDLL Successfully deleted")


circularDouble = CircularDoubleLinkedList()
print(circularDouble.create(4))
circularDouble.insert(3, 0)
circularDouble.insert(7, 1)
circularDouble.insert(2, 2)
circularDouble.insert(6, 3)
print([node.value for node in circularDouble])
print(circularDouble.search(2))
circularDouble.traverse()
circularDouble.delete(0)
circularDouble.reverse_traverse()
circularDouble.delete_entirely()
print([node.value for node in circularDouble])
