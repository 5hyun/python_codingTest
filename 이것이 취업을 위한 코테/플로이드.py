#노드 개수 입력
#간선 개수 입력
#graph에 2차원 리스트
#간선 정보 입력
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, (n+1)):
    for a in range(1, (n+1)):
        for b in range(1, (n+1)):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, (n+1)):
    for j in range(1, (n+1)):
        print(graph[i][j], end=' ')
    print()
