n = int(input())
a = input().split()
 
for i in range(n): #입력된거 정수형으로 변환
    a[i] = int(a[i])

s = [0] * 23 #s에 0인 것을 24개 만든다.

for i in range(n):
    j = a[i]
    s[j-1] += 1

for i in range(24):
    print(s[i], end = ' ')