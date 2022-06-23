n, m = map(int, input().split())
ary = []

for i in range(n):
    ary.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
# 동전 수만큼 반복
for i in range(n):
    # 가장 작은 동전 수부터 구하려는 목표 수까지 반복
    for j in range(ary[i], m+1):
        # (i-k)원을 만들 수 있으면
        if d[j - ary[i]] != 10001:
            d[j] = min(d[j], d[j-ary[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])