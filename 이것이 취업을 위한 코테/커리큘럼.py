from collections import deque
import copy

n = int(input())

indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]
weight = [0] * (n+1)

for i in range(1, n+1):
    ary = list(map(int, input().split()))
    weight[i] = ary[0]

    for j in range(1, len(ary)):
        if ary[j] == -1:
            break
        indegree[i] += 1
        graph[ary[j]].append(i)

result = copy.deepcopy(weight)

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        result[i] = max(result[i], result[now] + weight[i])

        if indegree[i] == 0:
            q.append(i)

for i in result:
    print(i)    
