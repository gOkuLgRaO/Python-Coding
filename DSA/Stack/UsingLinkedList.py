"""
PUSH - add nodes at the beginning
POP - remove nodes from the beginning
PEEK - return the head value
isEmpty() - if head is None or not
DELETE - set head reference to None
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Stack:
    def __init__(self):
        self.stack_linked_list = StackLinkedList()

    def __str__(self):
        values = [str(node.value) for node in self.stack_linked_list]
        return " -> ".join(values)

    def is_empty(self):
        return self.stack_linked_list.head is None

    def push(self, value):
        node = Node(value)
        node.next = self.stack_linked_list.head
        self.stack_linked_list.head = node

    def pop(self):
        if self.is_empty():
            return "There are no elements"
        else:
            value = self.stack_linked_list.head.value
            self.stack_linked_list.head = self.stack_linked_list.head.next
            return value

    def peek(self):
        if self.is_empty():
            return "There are no elements"
        else:
            value = self.stack_linked_list.head.value
            return value

    def delete(self):
        self.stack_linked_list.head = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.pop()
customStack.peek()
print(customStack)
customStack.delete()
print(customStack)
