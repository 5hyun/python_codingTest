n, m = map(int, input().split())
start = int(input())
INF = int(1e9)

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    index = -1
    min = INF
    for i in range(1, n+1):
        if distance[i] < min and not visited[i]:
            min = distance[i]
            index = i
    return index

def dijkstra(start):
    visited[start] = True
    distance[start] = 0

    for j in graph[start]:
        distance[j[0]] = j[1]

    for j in range(n-1):
        cost = get_smallest_node()
        visited[cost] = True
        
        for k in graph[cost]:
            weight = distance[cost] + k[1]

            if distance[k[0]] > weight:
                distance[k[0]] = weight

dijkstra(start)

print(distance)