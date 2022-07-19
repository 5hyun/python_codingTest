n = input()
ary = []

for i in range(len(n)):
    ary.append(int(n[i]))

left = 0
right = 0

mid = len(n) // 2

for i in range(mid):
    left += ary[i]

for i in range(mid, len(n)):
    right += ary[i]

if left == right:
    print("LUCKY")
else:
    print("READY")