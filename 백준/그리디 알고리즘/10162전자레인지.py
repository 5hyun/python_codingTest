x = input()
len_x = len(x)

if(x[len_x-1]!='0'):
    print("-1")
else:
    x = int(x)
    n_300 = 0
    n_60 = 0
    n_10 = 0

    n_300 = x // 300
    x %= 300
    n_60 = x // 60
    x %= 60
    n_10 = x // 10

    print(n_300, n_60, n_10, end = ' ')