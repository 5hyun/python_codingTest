import heapq

n = int(input())
ary = []
heap = []
rst = []
for i in range(n):
    x = int(input())
    ary.append(x)
for i in range(n):
    if ary[i] == 0:
        if heap:
            rst.append(heapq.heappop(heap)[1])
        else:
            rst.append(0)
    else:
        heapq.heappush(heap, (-ary[i], ary[i]))
for i in rst:
    print(i)