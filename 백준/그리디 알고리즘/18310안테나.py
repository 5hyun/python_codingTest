n = int(input())
ary = list(map(int, input().split()))
m = len(ary)//2 - 1
l = m + 1
ary.sort()
sum1 = 0
sum2 = 0
for i in range(n):
    if i == m:
        continue
    sum1 += abs(ary[m] - ary[i])
for i in range(n):
    if i == l:
        continue
    sum2 += abs(ary[l] - ary[i])
print(ary[m if sum1 <= sum2 else l])