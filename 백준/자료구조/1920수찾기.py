n = int(input())
ary = list(map(int, input().split()))
m = int(input())
s = list(map(int, input().split()))
for i in range(m):
    if s[i] in ary:
        print(1)
    else:
        print(0)