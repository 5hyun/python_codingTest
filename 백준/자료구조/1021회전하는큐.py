from collections import deque

n, m = map(int, input().split())
ary = list(map(int, input().split()))
num = deque()
for i in range(n):
    num.append(i+1)
l = 0
count = 0
while(True):
    if ary[l] == num[0]:
        num.popleft()
        l += 1
        if l == m:
            break
    else:
        t = num.index(ary[l])
        if t <= len(num)//2:
            temp = num.popleft()
            num.append(temp)
            count += 1
        else:
            temp = num.pop()
            num.appendleft(temp)
            count += 1
print(count)