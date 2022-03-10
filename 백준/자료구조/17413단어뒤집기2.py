x = input()
ary = ''
rst = ''
for i in range(len(x)):
    if x[i] == '<':
        if ary != '':
            rst += ary[::-1]
            ary = ''
        ary += x[i]
    elif x[i] == ' ':
        if ary:
            if ary[0] == '<':
                ary += ' '
                continue
        rst += ary[::-1] + ' '
        ary = ''
    elif x[i] == '>':
        ary += x[i]
        rst += ary
        ary = ''
    else:
        ary += x[i]
if ary:
    rst += ary[::-1]
print(rst)