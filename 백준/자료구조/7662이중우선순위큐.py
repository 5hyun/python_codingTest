import heapq

t = int(input())
rst = []
for i in range(t):
    n = int(input())
    chk = [False]*1_000_001
    max = []
    min = []
    for j in range(n):
        x = list(input().split())
        if x[0] == 'I':
            heapq.heappush(max, (-int(x[1]), j))
            heapq.heappush(min, (int(x[1]), j))
            chk[j] = True
        else:
            if x[1] == '1':
                while max and not chk[max[0][1]]: heapq.heappop(max)
                if max:
                    chk[max[0][1]] = False
                    heapq.heappop(max)
            else:
                while min and not chk[min[0][1]]: heapq.heappop(min)
                if min:
                    chk[min[0][1]] = False
                    heapq.heappop(min)
    
    while max and not chk[max[0][1]]: heapq.heappop(max)
    while min and not chk[min[0][1]]: heapq.heappop(min)

    rst.append([])
    if max and min:
        m = max[0][0]
        rst[i].append(-max[0][0])
        rst[i].append(min[0][0])
    else:
        rst[i].append("EMPTY")
for i in rst:
    if len(i) == 1:
        print(i[0])
    else:
        print('{} {}'.format(i[0], i[1]))
