n, k = map(int, input().split())
ary = []
rst = []
for i in range(n):
    ary.append(i+1)
t = k -1
while(True):
    if(len(rst) == n):
        break
    if t < len(ary):
        a = ary[t]
        del ary[t]
        rst.append(a)
        t += k-1
    else:
        t %= len(ary)
        a = ary[t]
        del ary[t]
        rst.append(a)
        t += k-1
print("<", end = '')
for i in rst:
    if i == rst[-1]:
        print(i, end = '')
    else:
        print(i, end = ', ')
print('>')