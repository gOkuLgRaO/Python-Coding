class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSingleLinkedList:
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
        newnode.next = newnode  # When there is only one node, The node calls itself, making it circular.
        self.head = newnode
        self.tail = newnode
        return "CSLL has been created"

    def insert(self, value, location):
        if self.head is None:
            return "Head reference is none"
        else:
            newnode = Node(value)
            if location == 0:
                newnode.next = self.head
                self.head = newnode
                self.tail.next = newnode
            elif location == 1:
                newnode.next = self.tail.next
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode
            return "Insertion successful"

    def traversal(self):
        if self.head is None:
            return "No head exists"
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next
                if tempnode == self.tail.next:
                    break

    def searching(self, value):
        if self.head is None:
            return "No head present"
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == value:
                    return tempnode.value
                tempnode = tempnode.next
                if tempnode == self.tail.next:
                    return "The node does not exist"

    def delete(self, location):
        if self.head is None:
            return "No head present"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempnode = self.head
                    while tempnode is not None:
                        if tempnode.next == self.tail:
                            break
                        tempnode = tempnode.next
                    tempnode.next = self.head
                    self.tail = tempnode
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = nextnode.next

    def delete_completely(self):
        self.head = None
        self.tail.next = None
        self.tail = None


circularSLL = CircularSingleLinkedList()
print(circularSLL.create(1))
circularSLL.insert(0, 0)
circularSLL.insert(5, 1)
circularSLL.insert(3, 2)
circularSLL.traversal()
print(circularSLL.searching(5))
circularSLL.delete(0)
print([node.value for node in circularSLL])
