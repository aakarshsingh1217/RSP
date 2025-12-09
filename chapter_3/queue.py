class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if not self.items:
            return None
        
        val = self.items[0]
        del self.items[0]

        return val