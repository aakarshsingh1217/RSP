class Stack:
    def __init__(self):
        self.items = []
        self.length = 0

    def push(self, val):
        self.items.append(val)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        
        last_index = self.length - 1
        val = self.items[last_index]
        del self.items[last_index]
        self.length -= 1
        
        return val