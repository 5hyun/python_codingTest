n = int(input())
ary = []
for i in range(n): 
    x = int(input())
    ary.append(x)
lst = []
rst = []
i = 0#ary
j = 1#rst
while(True):
    if lst and lst[-1] == ary[i]:
       rst.append('-')
       lst.pop()
       i += 1
       continue
    if j == n+1:
        break
    lst.append(j)
    j += 1
    rst.append('+')
test = []
bol = []
l = 1
k = 0
for i in rst:
    if i == '+':
        test.append(l)
        l += 1
    else:
        t = test.pop()
        if t == ary[k]:
            bol.append(t)
            k += 1
        else:
            break    
if ary == bol:
    for i in rst:
        print(i)
else:
    print('NO')