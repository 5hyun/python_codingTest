ary = []
for i in range(10):
    ary.append([])
    for j in range(10):
        ary[i].append(0)

for i in range(10):
    a = input().split()
    for j in range(10):
        ary[i][j] = int(a[j])#이 부분 주의 깊게 보기

x = 1
y = 1
while(True):
    if(x == 9 and y == 8):
        break
        
    if(ary[x][y]==0):
        ary[x][y] = 9
        y += 1
    elif(ary[x][y]==2):
        ary[x][y] = 9
        break
    elif(ary[x][y]==1):
        x += 1
        y -= 1

for i in range(10):
    for j in range(10):
        print(ary[i][j], end = ' ')
    print()