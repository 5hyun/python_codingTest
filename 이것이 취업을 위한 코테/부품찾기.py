# 이진 탐색
def binary(ary, target, start, end):
    left = start
    mid = (start + end) // 2
    right = end
    
    if left > right:
        return "no"
    
    if target == ary[mid]:
        return "yes"
    elif target < ary[mid]:
        return binary(ary, target, left, mid-1)
    else:
        return binary(ary, target, mid+1, right)

n = int(input())
ary = list(map(int, input().split()))
ary.sort()

m = int(input())
chk = list(map(int, input().split()))

answer = []
for i in range(m):
    answer.append(binary(ary, chk[i], 0, n-1))
    
for i in range(m):
    print(answer[i], end = " ")

