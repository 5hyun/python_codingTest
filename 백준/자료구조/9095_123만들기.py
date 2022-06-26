t = int(input())
ary = []

for i in range(t):
    ary.append(int(input()))


d = [0] * 11

def a(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    else:
        return a(n-1) + a(n-2) + a(n-3)

for i in range(t):
    print(a(ary[i]))