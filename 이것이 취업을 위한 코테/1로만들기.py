# #내가 풀어본 비효율적인 방식
# from collections import deque

# x = int(input())
# answer = 0

# q = deque([(x, 0), (x-1, 1)])
# while True:
#     t = q.popleft()
#     nx = t[0]
#     count = t[1]

#     if nx == 1:
#         answer = count
#         break

#     if (nx % 5) == 0:
#         q.append((nx // 5, count+1))
#         q.append(((nx // 5) - 1, count+2))
#     if (nx % 3) == 0:
#         q.append(((nx // 3) - 1, count+2))
#     if (nx % 2) == 0:
#         q.append(((nx // 2) - 1, count+2))

# print(answer)

# 교재 풀이
x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])