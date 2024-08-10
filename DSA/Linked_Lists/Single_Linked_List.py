class Node:
    # a node consists of value and address of next node.
    def __init__(self, value=None):  # Take value of the node as input
        self.value = value
        self.next = None


class SingleLinkedList:
    # a singly linked list consists of head and tail
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head  # Start with the head node
        while node:  # Continue as long as there is a node
            yield node  # Yield the current node
            node = node.next  # Move to the next node

    def insert(self, value, location):  # take input of value and location of insertion
        newnode = Node(value)  # create a new node
        if self.head is None:  # check if head exists or not
            self.head = newnode  # if not, make this node as head and tail
            self.tail = newnode
        else:
            if location == 0:  # add at the beginning of the SLL
                newnode.next = self.head
                self.head = newnode
            elif location == 1:  # add at the end of the SLL
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            else:  # add at the middle of the SLL
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

    def traverse(self):
        if self.head is None:
            print("The linked list doesnt exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def search(self, value):
        if self.head is None:
            return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return node.value
                node = node.next
            return "The value does not exist"

    def delete(self, location):
        if self.head is None:
            print("Does not exist")
        else:
            if location == 0:  # If you want to delete the first node
                if self.head == self.tail:  # check if there is only one node
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next  # move the head to next node
            elif location == 1:  # If you want to delete the last node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = nextnode.next

    def delete_entire_sll(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None


singlyLinkedList = SingleLinkedList()
singlyLinkedList.insert(1, 1)
singlyLinkedList.insert(2, 1)
singlyLinkedList.insert(3, 1)
singlyLinkedList.insert(0, 0)
singlyLinkedList.insert(0, 3)
print(singlyLinkedList.search(3))
singlyLinkedList.traverse()
singlyLinkedList.delete(0)
print([node.value for node in singlyLinkedList])
