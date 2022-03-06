import heapq

heap = []
rst = []
n = int(input())
for i in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    elif len(heap) == 0:
        rst.append(0)
    else:
        t = heapq.heappop(heap)[1]
        rst.append(t)
for i in rst:
    print(i)