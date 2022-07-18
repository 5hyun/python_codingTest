from collections import deque

n = int(input())
ary = list(map(int, input().split()))

ary.sort()
ary = deque(ary)

answer = 0

while ary:
    max = ary.pop() - 1

    while True:
        if ary:
            ary.popleft()
            max -= 1

            if max == 0:
                answer += 1
                break
        else:
            break

print(answer)