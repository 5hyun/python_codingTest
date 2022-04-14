import heapq

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
indegree = [0 for i in range(n+1)]
queue = []
answer = []

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)
        
while(queue):
    t = heapq.heappop(queue)
    answer.append(t)
    for i in graph[t]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(queue, i)

for i in answer:
    print(i, end = " ")