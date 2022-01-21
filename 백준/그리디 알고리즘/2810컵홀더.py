n = int(input())
x = input()
x = x.replace('LL', 'S')
l = len(x) + 1
print(min(l, n))