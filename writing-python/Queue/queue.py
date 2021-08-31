from collections import deque

queue = deque()

queue.append('a')
queue.append('b')
queue.append('c')
print(queue)
queue.popleft()
print(queue)