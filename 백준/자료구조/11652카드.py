n = int(input())
dic = {}
for i in range(n):
    x = int(input())
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
ary = sorted(dic.items(), key=lambda x: x[1], reverse = True)
t = ary[0][1]
rst = [ary[0][0]]
for i in range(1, len(ary)):
    if ary[i][1] == t:
        rst.append(ary[i][0])
    else:
        break
print(min(rst))