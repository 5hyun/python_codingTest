'''
ary = []
while(True):
    sum = 0
    a, b, c = map(int, input().split())
    if((a==0 and b == 0 and c == 0) or a >= c or a >= b or b >= c):
        break
    sum += (c//b) * a
    if((c%b)<a):
        sum += c%b
    elif((c%b)>a):
        sum += a
    ary.append(sum)
lena = len(ary)
for i in range(0, lena):
    print('Case %d: %d'%(i+1, ary[i]))
'''
ary = []
while(True):
    L, P, V = map(int, input().split())
    if(L+P+V == 0):
        break
    sum = (V//P) * L + min(V%P, L)
    ary.append(sum)

for i in range(len(ary)):
     print('Case %d: %d'%(i+1, ary[i]))