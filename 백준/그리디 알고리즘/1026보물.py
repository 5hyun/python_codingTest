n = int(input())
a = input().split()
b = input().split()

a = list(map(int, a))#리스트 정수형으로 변환
b = list(map(int, b))
a.sort()
b.sort()

s = []
for i in range(n):
    mul = a[i] * b[n-1-i]
    s.append(mul)
sum = 0
for i in range(n):
    sum += s[i]
print(sum)