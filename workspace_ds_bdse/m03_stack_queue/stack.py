class Node:
    def __init__(self, data, next_):
        self.data = data
        self.next = next_

class Stack:
    def __init__(self, top = None):
        self.top = top

    def is_empty(self):
        return self.top is None

    def push(self, value):
        node = Node(value, self.top)
        self.top = node

    def pop(self):
        if self.is_empty():
            print("The Stack is empty!")
            return None
        temp = self.top.data
        self.top = self.top.next
        return temp

import random
stack = Stack()
for i in range(10):
    stack.push(random.randint(0, 32768) % 100)
while not stack.is_empty():
    print("Pop data is", stack.pop())
stack.pop()

