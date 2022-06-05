from collections import deque

n = int(input())
ary = []
for i in range(n):
    ary.append(list(map(int, input())))
    
#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    ary[x][y] = 0
    count = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if ary[nx][ny] == 1:
                ary[nx][ny] = 0
                q.append((nx, ny))
                count += 1
    return count

chk = []
for i in range(n):
    for j in range(n):
        if ary[i][j] == 1:
            chk.append(bfs(i, j))

chk.sort()
print(len(chk))
for i in chk:
    print(i)
            