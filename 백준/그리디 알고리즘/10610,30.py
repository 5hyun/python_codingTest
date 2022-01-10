a = input()
a = list(map(int,list(a)))
sum = 0
lena = len(a)
for i in range(lena):
    sum += a[i]
a.sort()

if(sum%3 != 0 or a[0]!=0):
    print("-1")
else:
    for i in range(lena-1, -1, -1):
        print(a[i], end = '')   