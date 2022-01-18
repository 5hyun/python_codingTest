import heapq

a, b = map(int,input().split())
ary = input().split()
ary = list(map(int, ary))
heapq.heapify(ary) #리스트를 힙으로 변환
for i in range(b):
    sum = ary[0]
    heapq.heappop(ary)
    sum += ary[0]
    heapq.heappop(ary)
    heapq.heappush(ary, sum)
    heapq.heappush(ary, sum)
sum = 0
for i in ary:
    sum += i
print(sum)