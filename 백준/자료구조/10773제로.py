n = int(input())
ary = []
for i in range(n):
    x = int(input())
    if x == 0:
        ary.pop()
    else:
        ary.append(x)
print(sum(ary))