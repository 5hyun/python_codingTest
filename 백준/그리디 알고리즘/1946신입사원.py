import sys

m = int(input())
sum = []
for i in range(m):
    n = int(input())
    ary = []
    for j in range(n):
        x = sys.stdin.readline().split()
        ary.append([])
        ary[j].append(int(x[0]))
        ary[j].append(int(x[1]))
    ary.sort()
    count = 1
    min = ary[0][1]
    for k in range(1, n):
        if min > ary[k][1]:
            min = ary[k][1]
            count += 1
    sum.append(count)
for i in sum:
    print(i)