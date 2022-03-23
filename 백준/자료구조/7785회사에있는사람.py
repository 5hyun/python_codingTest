n = int(input())
dic = {}
for i in range(n):
    x, y = input().split()
    if y == 'enter':
        dic[x] = 1
    else:
        dic[x] = 0
dic = sorted(dic.items(), reverse = True)
for i in dic:
    if i[1] == 1:
        print(i[0])