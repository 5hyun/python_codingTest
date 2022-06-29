n = int(input())
ary = []
for i in range(n):
    start, end = map(int, input().split())
    ary.append((start, end))
    
ary.sort()
ary = sorted(ary, key=lambda x : x[1])

endTime = ary[0][1]
count = 1

for i in range(1, n):
    if ary[i][0] >= endTime:
        count += 1
        endTime = ary[i][1]

print(count)