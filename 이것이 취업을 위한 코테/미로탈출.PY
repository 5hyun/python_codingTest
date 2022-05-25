from collections import deque

n, m = map(int, input().split())
ary = []
for i in range(n):
    ary.append(list(map(int, input())))
    
#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        #상하좌우 방문
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            #범위 벗어나면 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            #괴물 만나면 continue
            if ary[nx][ny] == 0:
                continue
            
            #한번도 방문하지 않은 곳이여야 체크한다.
            if ary[nx][ny] == 1:
                ary[nx][ny] = ary[x][y] + 1
                q.append((nx, ny))
    return ary[n-1][m-1]

print(bfs(0,0))