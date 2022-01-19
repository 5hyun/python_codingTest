import heapq

n = int(input())
ary = []
for i in range(n):
    x = int(input())
    ary.append(x)
count = 0
heapq.heapify(ary)
j = 1
for i in range(n):
    if(ary[0] == j):
        heapq.heappop(ary)
        j += 1
        continue
    else:
        count += abs(ary[0] - j)
        heapq.heappop(ary)
        j += 1
        
print(count)