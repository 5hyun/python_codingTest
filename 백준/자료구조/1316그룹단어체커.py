n = int(input())
ary = []
for i in range(n):
    ary.append(input())
    
count = n
for i in range(n):
    dic = []
    t = ary[i]
    for j in range(len(t)):
        if t[j] not in dic:
            dic.append(t[j])
        elif (t[j-1] == t[j]):
            continue
        else:
            count -= 1
            break
print(count)