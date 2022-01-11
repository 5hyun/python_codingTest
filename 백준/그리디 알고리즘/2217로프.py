'''처음에 풀었던 풀이
n = int(input())
ary = []
for i in range(n):
    x = int(input())
    ary.append(x)
ary.sort()
mul = ary[0] * n
s = []
c = 0
for i in range(n):
    if(ary[n-1-i]>mul):
        s.append(ary[n-1-i])
        c += 1
lens = len(s)
sum = 0
if(lens>0):
    for i in range(lens):
       sum += s[i]
    print(int(sum/c))
else:
    print(mul) 
'''
n = int(input())
ary = []
for i in range(n):
    x = int(input())
    ary.append(x)
ary.sort(reverse = True)
s = []
for i in range(n):
    s.append(ary[i] * (i+1))
print(max(s))