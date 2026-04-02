class Node:
    def __init__(self, data, next_ = None):
        self.data = data
        self.next = next_

class Queue:
    def __init__(self, front = None, rear = None):
        self.front = front
        self.rear = rear

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.is_empty():
            print("The Queue is empty!")
            return None
        temp = self.front.data
        self.front = self.front.next
        return temp

import random
queue = Queue()
for i in range(10):
    queue.enqueue(random.randint(0, 32768) % 100)

while not queue.is_empty():
    print("Dequeue data is", queue.dequeue())
queue.dequeue()
