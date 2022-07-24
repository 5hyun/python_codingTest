from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
ary = list(map(int, input().split()))

answer = bisect_right(ary, x) - bisect_left(ary, x)

if answer == 0:
    print(-1)
else:
    print(answer)