from collections import deque

n = int(input())
m = int(input())

dic = {}
for i in range(m):
    a, b = map(int, input().split())
    if a not in dic:
        dic[a] = [b]
    else:
        dic[a].append(b)
    if b not in dic:
        dic[b] = [a]
    else:
        dic[b].append(a)

q = deque()
for i in dic[1]:
    q.append(i)

result = []
while q:
    t = q.popleft()
    if t not in result:
        result.append(t)
    if t in dic:
        for i in dic[t]:
            if i in result:
                continue
            q.append(i)

print(len(result)-1)