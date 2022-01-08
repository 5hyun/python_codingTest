n, k = map(int,input().split())

ary = []
for i in range(n):
    x = int(input())
    ary.append(x)

count = 0
for i in range(n-1, -1, -1):
    if(k >= ary[i]):
        count += k // ary[i]
        k %= ary[i]
print(count)