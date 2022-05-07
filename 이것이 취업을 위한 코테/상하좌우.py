N = int(input())
dis = list(input().split())

cur = [1,1]
for i in dis:
    if i == "L":
        cur[1] -= 1
        if cur[1] < 1:
            cur[1] += 1
    elif i == "R":
        cur[1] += 1
        if cur[1] > N:
            cur[1] -= 1
    elif i == "U":
        cur[0] -= 1
        if cur[0] < 1:
            cur[0] += 1
    else:
        cur[0] += 1
        if cur[0] > N:
            cur[0] -= 1
print('%d %d'%(cur[0], cur[1]))