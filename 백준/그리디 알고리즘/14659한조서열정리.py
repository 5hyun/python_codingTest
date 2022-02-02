n = int(input())
x = input().split()
x = list(map(int, x))
max1 = x[0]
count = 0
base = 0
for i in range(1, n):
    if max1 > x[i]:
        count += 1
    elif max1 < x[i]:
        max1 = x[i]
        count = 0
    base = max(base, count)
print(base)
