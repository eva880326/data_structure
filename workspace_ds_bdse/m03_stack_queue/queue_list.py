class Queue:
    def __init__(self):
        self.arr = []

    def is_empty(self):
        return len(self.arr) == 0
        
    def enqueue(self, value):
        self.arr.append(value)
    
    def dequeue(self):
        if self.is_empty():
            print("The Queue is empty!")
            return None
        return self.arr.pop(0)

import random
queue = Queue()
for i in range(10):
    queue.enqueue(random.randint(0, 32768) % 100)

while not queue.is_empty():
    print("Dequeue data is", queue.dequeue())
queue.dequeue()
