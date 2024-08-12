"""
creation of stack using python lists is not recommended because as the size of the stack increases,
the performance decreases.
It's better to use Linked Lists for stack operation
"""


class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.list = []

    def __str__(self):
        if self.list is None:
            return "Stack has been deleted"
        values = reversed(self.list)
        values = [str(x) for x in values]
        return "\n".join(values)

    def is_empty(self):
        return not self.list

    def is_full(self):
        return len(self.list) == self.maxsize

    def push(self, value):
        if self.is_full():
            return "Stack is full"
        else:
            self.list.append(value)
            return "The element has been inserted"

    def pop(self):
        if self.is_empty():
            return "There are no elements to pop"
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return "There is no element"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None
        print("Deleted the stack")


customStack = Stack(5)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.pop()
print(customStack.peek())
print(customStack)
customStack.delete()
print(customStack)
