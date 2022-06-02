def binary_search(array, target, start, end):
    mid = (start + end) // 2
    if start > end:
        return None
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
        
n = int(input())
ary = list(map(int, input().split()))
ary.sort()
m = int(input())
lst = list(map(int, input().split()))
chk = [0] * m

for i in range(m):
    x = binary_search(ary, lst[i], 0, n-1)
    if x == None:
        continue
    else:
        chk[i] = 1

for i in chk:
    print(i, end = " ")