class Stack:
    def __init__(self, ary):    
        self.ary = []
    def push(self, ary, item):
        ary.append(item)
    def pop(self, ary):
        if ary:
            t = ary[len(ary)-1]
            del ary[len(ary)-1]
            return t
        else:
            return -1
    def size(self, ary):
        return len(ary)
    def empty(self, ary):
        if ary:
            return 0
        else:
            return 1
    def top(self, ary):
        if ary:
            return ary[len(ary)-1]
        else:
            return -1
a = []
rst = []
s = Stack(a)
n = int(input())
for i in range(n):
    x = input().split()
    if x[0] == 'push':
        s.push(a, x[1])
    elif x[0] == 'pop':
        rst.append(s.pop(a))
    elif x[0] == 'size':
        rst.append(s.size(a))
    elif x[0] == 'empty':
        rst.append(s.empty(a))
    elif x[0] == 'top':
        rst.append(s.top(a))
for i in rst:
    print(i)      