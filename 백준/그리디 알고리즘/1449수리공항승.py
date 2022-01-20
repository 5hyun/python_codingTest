N, L = map(int, input().split())
ary = []
x = input().split()
for i in range(len(x)):
        ary.append(int(x[i]))
ary.sort()
chk = ary[0] + L - 0.5
count = 1
for i in range(1, N):
    if(ary[i] <= chk):
        continue
    else:
        chk = ary[i] + L - 0.5
        count += 1
print(count)