n, m = map(int, input().split())
ary = []
for i in range(n):
    ary.append(int(input()))

start = 1
end = max(ary)
answer = 0

while (start <= end):
    mid = (start+end) // 2
    
    total = 0
    for i in range(n):
        if ary[i] >= mid:
            total += ary[i] // mid
               
    #너무 짧게 짤랐다.
    if total >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)
        