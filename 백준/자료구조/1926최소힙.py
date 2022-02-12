import heapq

n = int(input())
que = []
rst = []
for i in range(n):
    x = int(input())
    if x == 0:
        if que:
            rst.append(heapq.heappop(que))
        else:
            rst.append(0)
    else:
        heapq.heappush(que, x)
for i in rst:
    print(i)