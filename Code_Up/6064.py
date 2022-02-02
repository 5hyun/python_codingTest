a, b, c = map(int, input().split())

#(a if a>b else b) if (a if a>b else b) else c 가장 큰 값 구하는 법
d = a if a<b else b
e = d if d<c else c
print(e)
