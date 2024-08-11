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


doubleLinkedList = DoubleLinkedList()
doubleLinkedList.create(5)
print([node.value for node in doubleLinkedList])
