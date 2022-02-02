ary =[[], [], [], []]
n = int(input())
for i in range(n):
    x = int(input())
    if x > 0:
        ary[0].append(x)
    elif x == 0:
        ary[1].append(x)
    else:
        ary[2].append(x)
ary[2].sort()
while(True):
    if(len(ary[2]) <= 1):
        break
    mul = ary[2][0] * ary[2][1]
    ary[3].append(mul)
    del ary[2][0]
    del ary[2][0]
ary[0].sort(reverse = True)
while(True):
    if(len(ary[0]) <= 1):
        break
    a = ary[0][0]
    b = ary[0][1]
    if(a == 1 or b == 1):
        mul = a + b
    else: 
        mul = a * b
    ary[3].append(mul)
    del ary[0][0]
    del ary[0][0]
if(len(ary[2]) > 0):   
    for i in range(len(ary[1])):
        if(len(ary[2]) == 0):
            break
        del ary[2][0]
result = sum(ary[0]) + sum(ary[2]) + sum(ary[3])
print(result)