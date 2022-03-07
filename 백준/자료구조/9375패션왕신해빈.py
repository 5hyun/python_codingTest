t = int(input())
rst = []

for i in range(t):
    n = int(input())
    ary = []
    for j in range(n):
        x = input().split()
        for k in range(len(ary)):
            if ary[k][0] == x[1]:
                ary[k][1] += 1
                break
        else:
            ary.append([x[1], 1])
    mul = 1
    for l in ary:
        mul *= (l[1]+1)
    rst.append(mul-1)
   
for i in rst:
    print(i)