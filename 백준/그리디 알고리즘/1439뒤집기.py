'''
n = input()
s = []
j = 0
for i in range(len(n)):
    if(i == len(n)-1):
        s.append(n[i])
        break
    if(n[i]==n[i+1]):
        continue
    else:
        s.append(n[j:i+1])
        j = i+1
c0 = 0
c1 = 0
for i in range(len(s)):
   if(s[i][0]=='0'):
        c0 += 1
   else:
       c1 += 1
print(min(c0, c1))
'''
S = input()
count = 0
for i in range(len(S)-1): #그냥 len(s)로 하면 밑에 if 문에서 범위 오류가 나기 때문이다
    if S[i] != S[i+1]: 
        count += 1
print((count + 1) // 2)