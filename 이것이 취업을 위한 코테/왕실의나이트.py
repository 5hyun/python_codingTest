x = input()
row = int(x[1])
column = int(ord(x[0])) - int(ord('a')) + 1
count = 0

ary = [(2, 1), (2, -1), (-2, 10), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
for i in ary:
    r = row + i[0]
    c = column + i[1]
    if r >= 1 and r <= 8 and c >= 1 and c <= 8:
        count += 1
print(count)