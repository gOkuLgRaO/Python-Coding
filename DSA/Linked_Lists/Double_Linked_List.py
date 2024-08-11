class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def create(self, value):
        newnode = Node(value)
        newnode.prev = None
        newnode.next = None
        self.head = newnode
        self.tail = newnode
        return "DLL created successfully"

    def insert(self, value, location):
        if self.head is None:
            return "The node cannot be inserted"
        newnode = Node(value)
        if location == 0:
            newnode.prev = None
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

        elif location == 1:
            newnode.next = None
            newnode.prev = self.tail
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
            newnode.next.prev = newnode  # newnode.next.prev means nextnode
            tempnode.next = newnode

    def traverse(self):
        if self.head is None:
            return "There is no element to travel"
        tempnode = self.head
        while tempnode:
            print(tempnode.value)
            tempnode = tempnode.next

    def reverse_traverse(self):
        if self.head is None:
            return "There is no element to travel"
        tempnode = self.tail
        while tempnode:
            print(tempnode.value)
            tempnode = tempnode.prev

    def search(self, value):
        if self.head is None:
            return "There is not any element in list"
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == value:
                    return tempnode.value
                tempnode = tempnode.next
            return "The node does not exist"

    def delete(self, location):
        if self.head is None:
            return "There are no elements to delete"
        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

        elif location == 1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

        else:
            tempnode = self.head
            index = 0
            while index < location - 1:
                tempnode = tempnode.next
                index += 1
            tempnode.next = tempnode.next.next
            tempnode.next.prev = tempnode
        print("The node has been successfully deleted")

    def delete_entirely(self):
        if self.head is None:
            return "The head is none"
        tempnode = self.head
        while tempnode:
            tempnode.prev = None
            tempnode = tempnode.next
        self.head = None
        self.tail = None
        print("DLL successfully deleted")


doubleLinkedList = DoubleLinkedList()
doubleLinkedList.create(5)
doubleLinkedList.insert(1, 0)
doubleLinkedList.insert(7, 1)
doubleLinkedList.insert(4, 1)
doubleLinkedList.insert(6, 2)
doubleLinkedList.search(7)
doubleLinkedList.traverse()
doubleLinkedList.reverse_traverse()
doubleLinkedList.delete(0)
print([node.value for node in doubleLinkedList])
