class Stack:
    def __init__(self):
        self.arr = []

    def is_empty(self):
        return len(self.arr) == 0
        
    def push(self, value):
        self.arr.append(value)
    
    def pop(self):
        if self.is_empty():
            print("The Stack is empty!")
            return None
        return self.arr.pop()

import random
stack = Stack()
for i in range(10):
    stack.push(random.randint(0, 32768) % 100)
while not stack.is_empty():
    print("Pop data is", stack.pop())
stack.pop()
