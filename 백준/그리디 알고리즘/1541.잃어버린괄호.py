'''import re

s = input()
ary = re.split(r'[- | +]', s)
#ary = list(map(int, list(ary)))
b = []
pm = []
for i in range(len(s)):
    if(s[i]=='-'or s[i]=='+'):
        b.append(s[i])
for i in range(len(ary)):
    pm.append(ary[i])
    if(i<len(b)):
        pm.append(b[i])
for i in range(1, len(pm), 2):
    if(i >= len(b)):
        break
    if(pm[i]=='-'):
        pm[i+2] = '-'
        i += 2
sum = int(pm[0])
for i in range(1, len(pm), 2):
    if(pm[i]=='+'):
        sum += int(pm[i+1])
    else:
        sum -= int(pm[i+1])
print(sum)
'''
n = input().split('-') # -를 기준으로 나누고 각자 더한다음 빼주면된다
ary = []
for i in n: #리스트 for문
    s = i.split('+') # 입력 받으면서 나눈걸 또 + 기준으로 나눠서
    sum = 0
    for j in s:
        sum+=int(j)
    ary.append(sum)
m = ary[0] #ary에 +있는거랑 없는거 다 들어갔기 때문에 ary[0] 더해줌
for i in range(1, len(ary)):
    m -= ary[i]
print(m)