n = int(input())
sum = 0
i = 1
count = 0

while(sum <= n):
    sum += i
    count += 1
    i += 1

print(count-1)