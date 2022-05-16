n, m = map(int, input().split())
ary = []

for i in range(n):
    x = list(map(int, input()))
    ary.append(x)

def dfs(x, y):
    #범위 체크
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    #방문했는지 체크
    if ary[x][y] == 1:
        return False
    #상하좌우 탐색
    ary[x][y] = 1
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1
print(count)