class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        if self.list is None:
            return "Queue has been deleted"
        values = [str(x) for x in self.list]
        return " <- ".join(values)

    def is_empty(self):
        return self.list == []

    def enqueue(self, value):
        self.list.append(value)
        return "The element is inserted at end"

    def dequeue(self):
        if self.is_empty():
            return "No elements in the queue"
        else:
            return self.list.pop(0)

    def peek(self):
        if self.is_empty():
            return "No elements in queue"
        else:
            return self.list[0]

    def delete(self):
        self.list = None


customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)
print(customQueue.dequeue())
print(customQueue.peek())
print(customQueue)
customQueue.delete()
print(customQueue)
