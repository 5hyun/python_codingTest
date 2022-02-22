n = int(input())
a = list(map(int, input().split()))
dic = {}
for i in range(n):
    if a[i] in dic:
        dic[a[i]] += 1
    else:
        dic[a[i]] = 1
m = int(input())
b = list(map(int, input().split()))
rst = []
for i in range(m):
    if b[i] in dic:
        rst.append(dic[b[i]])
    else:
        rst.append(0)
for i in rst:
    print(i, end = ' ')