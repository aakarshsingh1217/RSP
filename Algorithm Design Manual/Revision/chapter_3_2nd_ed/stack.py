class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if (self.is_empty()):
            print("Pop from empty stack.")

            return
        
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0