x = list(input())
len_x = len(x)
x.sort()

dic = {}
for i in range(len_x):
    t = x[i]
    if t in dic:
        dic[t] += 1
    else:
        dic[t] = 1

chk = True
lst = list(dic)
answer = ""
len_chr = []
#짝수
if (len_x % 2) == 0:
    for i in dic:
        if (dic[i] % 2) == 1:
            chk = False
            break
        len_chr.append(dic[i] // 2)
    for i in range(len(len_chr)):
        answer += lst[i] * len_chr[i]
    for i in range(len(len_chr)-1, -1, -1):
        answer += lst[i] * len_chr[i]
#홀수
else:
    odd = ""
    for i in dic:
        if (dic[i] % 2) == 1:
            odd += i
            dic[i] -= 1
            if len(odd) > 1:
                chk = False
                break
        len_chr.append(dic[i] // 2)
        
    for i in range(len(len_chr)):
        answer += lst[i] * len_chr[i]
    answer += odd
    for i in range(len(len_chr)-1, -1, -1):
        answer += lst[i] * len_chr[i]

if chk:
    print(answer)
else:
    print("I'm Sorry Hansoo")