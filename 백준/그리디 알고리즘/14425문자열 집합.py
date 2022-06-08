n, m = map(int, input().split())

ary = []
for i in range(n):
    ary.append(input())

count = 0
for i in range(m):
    x = input()
    if x in ary:
        count += 1
print(count)