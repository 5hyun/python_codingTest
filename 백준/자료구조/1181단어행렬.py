n = int(input())

ary = []
for i in range(n):
    x = input()
    if x not in ary:
        ary.append(x)

ary.sort()
cnt = [] #(길이, 문자)
for i in range(len(ary)):
    t = ary[i]
    cnt.append((len(t), t))

cnt.sort()
for i in range(len(cnt)):
    print(cnt[i][1])