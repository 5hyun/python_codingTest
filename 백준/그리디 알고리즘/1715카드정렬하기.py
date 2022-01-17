import heapq

n = int(input())
heap = []
for i in range(n):
    x = int(input())
    heapq.heappush(heap, x)
result = 0
while(len(heap) != 1):
    sum = 0
    a = heap[0]
    heapq.heappop(heap)
    a += heap[0]
    heapq.heappop(heap)
    sum += a
    result += sum
    heapq.heappush(heap, sum)
    
print(result)