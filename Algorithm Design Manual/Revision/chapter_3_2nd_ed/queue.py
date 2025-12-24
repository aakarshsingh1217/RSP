from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if (self.is_empty()):
            print("Dequeue from empty queue.")

            return
        
        return self.items.popleft()
    
    def is_empty(self):
        return len(self.items) == 0