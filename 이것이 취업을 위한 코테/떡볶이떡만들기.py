# n, m = map(int, input().split())
# ary = list(map(int, input().split()))
# ary.sort()

# def search(ary, target, start, end):
#     mid = (start + end) // 2
#     sum = 0
#     for i in range(n):
#         t = ary[i] - mid
#         if t > 0:
#             sum += t
        
#     if sum == target:
#         return mid
#     elif sum > target:
#         return search(ary, target, mid + 1, end)
#     else:
#         return search(ary, target, start, mid-1)
    
# print(search(ary, m, 0, ary[-1]-1))

#책 풀이(반복적 풀이)
n, m = map(int, input().split())
ary = list(map(int, input().split()))

start = 0
end = max(ary)
result = 0

while (start <= end):
    total = 0
    mid = (start + end) // 2
    
    for i in range(n):
        if ary[i] - mid > 0:
            total += ary[i] - mid
        
    if m > total:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)