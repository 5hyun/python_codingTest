n = int(input())
ary = []
for i in range(n):
    x = int(input())
    ary.append(x)
ary.sort(reverse = True)
sum = 0
count = 1
for i in range(n):
    sum += ary[i] - (count - 1)
    count += 1
print(sum)