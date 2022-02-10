from collections import deque
n = int(input())
ary = deque()
for i in range(1, n+1):
    ary.appendleft(i)
while(len(ary) != 1):
    ary.pop()
    if(len(ary) > 1):
        t = ary.pop()
        ary.appendleft(t)
print(ary[0])