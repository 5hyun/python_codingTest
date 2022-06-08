x = input()
x = x.upper()

dic = {}
for i in range(len(x)):
    if x[i] not in dic:
        dic[x[i]] = 1
    else:
        dic[x[i]] += 1

dic = sorted(dic.items(), key = lambda x: x[1], reverse=True)

if len(x) > 1:
    if dic[0][1] == dic[1][1]:
        print("?")
    else:
        print(dic[0][0])
else:
    print(dic[0][0])