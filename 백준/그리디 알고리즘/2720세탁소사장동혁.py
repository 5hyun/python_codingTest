n = int(input())
ary = []
for i in range(n):
    x = int(input())
    p25 = 0
    p10 = 0
    p5 = 0
    p1 = 0
    
    p25 = x // 25
    x %= 25
    p10 = x // 10
    x %= 10
    p5 = x // 5
    p1 = x % 5
    
    ary.append([])
    ary[i].append(p25)
    ary[i].append(p10)
    ary[i].append(p5)
    ary[i].append(p1)
for i in range(len(ary)):
    for j in range(4):
        print(ary[i][j], end = " ")
    print()