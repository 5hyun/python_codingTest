from collections import deque

n, m = map(int, input().split())
ary = []
for i in range(n):
    ary.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if ary[nx][ny] == 0:
                continue
            
            if ary[nx][ny] == 1:
                ary[nx][ny] = ary[x][y] + 1
                q.append((nx, ny))
    
    return ary[n-1][m-1]

print(bfs(0,0))