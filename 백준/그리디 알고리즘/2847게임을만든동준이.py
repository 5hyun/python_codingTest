n = int(input())
ary = []
for i in range(n):
    x = int(input())
    ary.append(x)
count = 0
for i in range(n-1, 0, -1):
    if(ary[i]>ary[i-1]):
        continue
    else:
        while(ary[i] <= ary[i-1]):
            ary[i-1] -= 1
            count += 1
print(count)