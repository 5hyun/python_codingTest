n = int(input())

ary = []
for i in range(n):
    x = int(input())
    ary.append(x)
ary.sort(reverse = True)
s = [[]]
j = 0
for i in range(n):
    if i != 0 and (i+1) % 3 == 0:
        s.append([])
        j += 1
        continue
    s[j].append(ary[i])
hap = 0
for i in range(len(s)):
    hap += sum(s[i])

print(hap)