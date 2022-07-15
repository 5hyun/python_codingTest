def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
edges = []

parent = [i for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
answer = 0
max = 0

for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        answer += cost
        max = cost
        
print(answer - max)