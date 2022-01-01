s = input()

s = ord(s) - ord('a')
x = ord('a')

for i in range(s+1):
    print(chr(x), end=' ')
    x += 1