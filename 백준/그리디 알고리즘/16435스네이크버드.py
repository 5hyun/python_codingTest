n, h = map(int, input().split())
ary = list(map(int, input().split()))
ary.sort()
for i in range(n):
    if(h >= ary[i]):
        h += 1
    else:
        break
print(h)