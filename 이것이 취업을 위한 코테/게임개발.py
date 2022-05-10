# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, dir = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def left():
    global dir 
    dir -= 1
    if dir == -1:
        dir = 3

count = 1
turn = 0
while True:
    left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] == 1
        x = nx
        y = ny
        count += 1
        trun = 0
        continue
    else:
        turn += 1
    if turn == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if array[nx][ny] == 0:
            #만약 육지이면 x y를 업데이트해서 다시 while문으로 보내버림
            x = nx
            y = ny
        else:
            break
        turn = 0
print(count)