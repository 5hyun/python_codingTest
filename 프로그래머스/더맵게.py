import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    sum = 0
    while scoville[0] < K:
        if len(scoville) <= 1:
            answer = -1
            break
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        sum = a + (b*2)
        heapq.heappush(scoville, sum)
        answer += 1
        
    return answer