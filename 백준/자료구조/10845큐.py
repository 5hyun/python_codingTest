from collections import deque
class Queue:
    def __init__(self, ary = deque()):
        self.ary = ary
    def push(self, ary, item):
        ary.appendleft(item)
    def pop(self, ary):
        if ary:
            t = ary.pop()
            return t
        else:
            return -1
    def size(self, ary):
        return len(ary)
    def empty(self, ary):
        if len(ary) == 0:
            return 1
        else:
            return 0
    def front(self, ary):
        if ary:
            return ary[len(ary)-1]
        else:
            return -1
    def back(self, ary):
        if ary:
            return ary[0]
        else:
            return -1
    
n = int(input())
a = deque()
q = Queue(a)
rst = []
for i in range(n):
    x = input().split()
    if x[0] == 'push':
        q.push(a, x[1])
    elif x[0] == 'pop':
        rst.append(q.pop(a))
    elif x[0] == 'size':
        rst.append(q.size(a))
    elif x[0] == 'empty':
        rst.append(q.empty(a))
    elif x[0] == 'front':
        rst.append(q.front(a))
    elif x[0] == 'back':
        rst.append(q.back(a))
for i in rst:
    print(i)