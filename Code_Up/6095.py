ary = []
for i in range(19):
    ary.append([]) #리스트 안에 다른 리스트 추가
    for j in range(19):
        ary[i].append(0)

a = int(input())

for i in range(a):
    x, y = map(int, input().split())
    if(ary[x-1][y-1] != 1): 
        ary[x-1][y-1] += 1

for i in range(19):
    for j in range(19):
        print(ary[i][j], end = ' ')
    print()