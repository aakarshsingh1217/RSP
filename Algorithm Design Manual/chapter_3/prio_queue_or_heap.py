class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2
    
    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def bubble_up(self, index):
        while index > 0:
            parent = self.parent(index)

            if (self.heap[index] < self.heap[parent]):
                self.swap(index, parent)
                index = parent
            else:
                break

    def insert(self, key):
        self.heap.append(key)
        self.bubble_up(len(self.heap) - 1)

    def find_min(self):
        if (not self.heap):
            return None
        
        return self.heap[0]