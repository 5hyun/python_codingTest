n, m = map(int, input().split())
p6 = []
p1 = []
for i in range(m):
    a, b = map(int, input().split())
    p6.append(a)
    p1.append(b)
p6.sort()
p1.sort()

if(n>=6):
    price1 = p6[0] * (n//6)
    price2 = price1
    price1 += p6[0]
    price3 = p1[0] * n
    
    n %= 6
    if(n > 0):
        price2 += p1[0] * n
    print(min(price1, price2, price3))
else:
    s1 = p1[0] * n
    s6 = p6[0]
    price = min(s1, s6)
    print(price)