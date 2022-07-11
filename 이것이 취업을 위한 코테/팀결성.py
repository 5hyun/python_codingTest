n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(n+1)]    
answer = []

for i in range(m):
    a, b, c = map(int, input().split())
    
    if a == 0:
        union(parent, b, c)
    else:
        if find_parent(parent, b) == find_parent(parent, c):
            answer.append("Yes")
        else:
            answer.append("NO")

for i in answer:
    print(i)