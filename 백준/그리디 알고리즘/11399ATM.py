n = int(input())
m = input().split()
for i in range(n):
    m[i] = int(m[i])

m.sort()
sum = 0
for i in range(n):
    for j in range(i+1):
        sum += m[j]
print(sum)