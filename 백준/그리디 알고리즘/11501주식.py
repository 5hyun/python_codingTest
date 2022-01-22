n = int(input())
ary = []
for i in range(n):
    m = int(input())
    x = input().split()
    x = list(map(int, x))
    max = x[m-1]
    sum = 0
    for j in range(m-2, -1, -1):
        if x[j] < max:
            sum += max - x[j]
        elif(x[j] > max):
            max = x[j]
    ary.append(sum)
for i in ary:
    print(i)