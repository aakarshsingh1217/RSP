# Decl.: Use deque from collections module
import collections
queue = collections.deque()

# You can init. with some vals.:
queue = collections.deque([1, 2, 3])

# Enqueueing/adding elems.:
queue.append(4)
queue.append(5)

# Dequeueing/removing elems.:
queue.popleft() # 1
queue.popleft() # 2

# Check elem. at front of queue (next elem to be removed):
queue[0] # 3

# Get size
len(queue) # 3

while queue:
    print(queue.popleft())

if not queue:
    print("Queue empty!")