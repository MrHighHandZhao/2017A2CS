#S3C2 Carl queue Opt3
from collections import deque
Queue = deque([1,2,3])
def pop():
    Queue.popleft()
def append(item):
    Queue.append(item)

pop()
append(5)
print(Queue)


