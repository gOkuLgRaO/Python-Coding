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
            if node.next == self.head:
                break
            node = node.next

    def create(self, value):
        newnode = Node(value)
        newnode.next = newnode  # When there is only one node, The node calls itself, making it circular.
        self.head = newnode
        self.tail = newnode
        return "CSLL has been created"


circularSLL = CircularSingleLinkedList()
circularSLL.create(1)
print(node.value for node in circularSLL)
