n = int(input())
x = input()
rst = []
for i in range(n):
    a = int(input())
    rst.append(a)
index = []
for i in range(len(x)):
    if x[i] == '+' or x[i] == '-' or x[i] == '*' or x[i] == '/':
        index.append(x[i])
    else:
        index.append(rst[ord(x[i])-ord('A')])
ary = []
for i in index:
    if i == '+' or i == '-' or i == '*' or i == '/':
        t1 = ary.pop()
        t2 = ary.pop()
        t3 = 0
        if i == '+':
            t3 = t2 + t1
        elif i == '-':
            t3 = t2 - t1
        elif i == '*':
            t3 = t2 * t1
        else:
            t3 = t2 / t1
        ary.append(t3)
    else:
        ary.append(i)
print('%.2lf'%ary[0])