import collections

# Declaration: use deque from collections module
queue = collections.deque()

# Can initialize it with some init vals.
queue = collections.deque([1, 2, 3])

# Enqueuing/adding elems.
queue.append(4)
queue.append(5)

# Dequeuing/removing elems.
queue.popleft() # 1
queue.popleft() # 2

# Check elem. at front of queue (next elem. to be removed)
queue[0] # 3

# Get size
len(queue) # 3