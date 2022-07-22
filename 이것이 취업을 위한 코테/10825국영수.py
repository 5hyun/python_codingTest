n = int(input())

ary = []

for i in range(n):
    a, b, c, d = input().split()
    ary.append((a,int(b),int(c),int(d)))

ary = sorted(ary, key = lambda x : x[0], reverse=True)
ary = sorted(ary, key = lambda x : x[3])
ary = sorted(ary, key = lambda x : x[2], reverse=True)
ary = sorted(ary, key = lambda x : x[1])

for i in range(n-1, -1, -1):
    print(ary[i][0])