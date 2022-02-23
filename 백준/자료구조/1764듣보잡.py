n, m = map(int, input().split())
dic = {}
count = 0
for i in range(n+m):
    x = input()
    if i < n:
        dic[x] = 0
    else:
        if x in dic:
            dic[x] = 1
            count += 1
print(count)
rst = []
for i in dic:
    if dic[i] == 1:
        rst.append(i)
rst.sort()
for i in rst:
    print(i)