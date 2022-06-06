from collections import deque

n = int(input())
ary = deque(i for i in range(1, n+1))

cnt = []
while ary:
    cnt.append(ary.popleft())
    if ary:
        t = ary.popleft()
        ary.append(t)

for i in cnt:
    print(i, end = " ")