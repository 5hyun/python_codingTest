n, m = map(int, input().split())
ary = list(map(int, input().split()))

start = 0
end = max(ary)
answer = 0

while (start <= end):
    mid = (start+end) // 2
    
    total = 0
    for i in range(n):
        if ary[i] > mid:
            total += ary[i] - mid
    
    if m > total:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid
print(answer) 