class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head  # Start with the head node
        while node:  # Continue as long as there is a node
            yield node  # Yield the current node
            node = node.next  # Move to the next node

    def insert(self, value, location):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:                  # add at the beginning of the SLL
                newnode.next = self.head
                self.head = newnode
            elif location == 1:                  # add at the end of the SLL
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            else:                                 # add at the middle of the SLL
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode
                if tempnode == self.tail:
                    self.tail = newnode


singlyLinkedList = SingleLinkedList()
singlyLinkedList.insert(1, 1)
singlyLinkedList.insert(2, 1)
singlyLinkedList.insert(3, 1)
singlyLinkedList.insert(0, 0)
singlyLinkedList.insert(0, 3)
print([node.value for node in singlyLinkedList])
