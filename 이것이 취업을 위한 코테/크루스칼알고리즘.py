def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [i for i in range(v+1)]

edges = []
for i in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

answer = 0
edges.sort()

for edge in edges:
    cost, start, end = edge

    if find_parent(parent, start) != find_parent(parent, end):
        answer += cost
        union_parent(parent, start, end)

print(answer)