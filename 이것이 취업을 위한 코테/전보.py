INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[INF] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

count = 0
time = 0
for i in graph[c]:
    if i == INF or i == 0:
        continue
    count += 1
    time = max(time, i)

print(count, time)