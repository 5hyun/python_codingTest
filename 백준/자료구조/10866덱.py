from collections import deque

class Deque:
    def __init__(self, ary = deque()):
        self.ary = ary
    def push_front(self, ary, item):
        ary.append(item)
    def push_back(self, ary, item):
        ary.appendleft(item)
    def pop_front(self, ary):
        if ary:
            t = ary[len(ary)-1]
            del ary[len(ary)-1]
            return t
        else:
            return -1
    def pop_back(self, ary):
        if ary:
            t = ary[0]
            del ary[0]
            return t
        else:
            return -1
    def size(self, ary):
        return len(ary)
    def empty(self, ary):
        if ary:
            return 1
        else:
            return 0
    def front(self, ary):
        if ary:
            return ary[len(ary)-1]
        else:
            -1
    def back(self, ary):
        if ary:
            return ary[0]
        else:
            -1
a = deque()
d = Deque(a)
n = int(input())
rst = []
for i in range(n):
    x = input().split()
    if x[0] == 'push_front':
        d.push_front(a, x[1])
    elif x[0] == 'push_back':
        d.push_back(a, x[1])
    elif x[0] == 'pop_front':
        rst.append(d.pop_front(a))
    elif x[0] == 'pop_back':
        rst.append(d.pop_back(a))
    elif x[0] == 'size':
        rst.append(d.size(a))
    elif x[0] == 'empty':
        rst.append(d.empty(a))
    elif x[0] == 'front':
        rst.append(d.front(a))
    elif x[0] == 'back':
        rst.append(d.back(a))
for i in rst:
    print(i)