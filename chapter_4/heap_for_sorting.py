PQ_SIZE = 16

class Heap:
    def __init__(self):
        # index 0 is unused to match Skiena's formulas
        self.heap = [None]
        self.n = 0

    def pq_parent(self, index):
        if (index == 1):
            return -1
        
        return index // 2

    def pq_left_child(self, index):
        return 2 * index

    def pq_right_child(self, index):
        return 2 * index + 1

    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp


def pq_insert(prio_q, item):
    if (prio_q.n >= PQ_SIZE):
        print("Warning: priority queue overflow!")
        
        return

    prio_q.n += 1
    # index = q.n
    prio_q.heap.append(item)
    bubble_up(prio_q, prio_q.n)


def bubble_up(prio_q, index):
    parent = prio_q.pq_parent(index)

    if (parent == -1):
        # root, stop
        return

    # If parent is larger (min-heap), swap
    if (prio_q.heap[parent] > prio_q.heap[index]):
        prio_q.swap(parent, index)
        bubble_up(prio_q, parent)

def extract_min(prio_q):
    min = -1

    if (prio_q.n <= 0):
        print("Warning: empty prio queue.")
    else:
        min = prio_q.heap[1]
        
        prio_q.heap[1] = prio_q.heap[prio_q.n]
        prio_q.heap.pop()
        prio_q.n -= 1
        bubble_down(prio_q, 1)

    return min

def bubble_down(prio_q, index):
    child_index = prio_q.pq_left_child(index)
    min_index = index

    for i in range(0, 1 + 1):
        if (child_index + i <= prio_q.n):
            if (prio_q.heap[min_index] > 
                prio_q.heap[child_index + i]):

                min_index = child_index + i

    if (min_index != index):
        prio_q.swap(index, min_index)
        bubble_down(prio_q, min_index)

def make_heap(arr, n):
    heap = Heap()

    for i in range(0, n):
        pq_insert(heap, arr[i])

    return heap

def heapsort(arr, n):
    new_heap = make_heap(arr, n)

    for i in range(0, n):
        arr[i] = extract_min(new_heap)

def make_heap_fast(prio_queue, arr, n):
    prio_queue.n = n

    prio_queue.heap = [None]
    for i in range(0, n):
        prio_queue.heap.append(arr[i])

    for i in range(prio_queue.n // 2, 0, -1):
        bubble_down(prio_queue, i)

def heap_compare(prio_queue, i, count, x):
    if ((count <= 0) or (i > prio_queue.n)):
        return count
    
    if (prio_queue.heap[i] < x):
        count = heap_compare(prio_queue, prio_queue.pq_left_child(i), count - 1, x)
        count = heap_compare(prio_queue, prio_queue.pq_right_child(i), count, x)

    return count