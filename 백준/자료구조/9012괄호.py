n = int(input())
rst = []
for i in range(n):
    ary = []
    x = input()
    for j in range(len(x)):
        if x[j] == "(":
            ary.append('(')
            if j == len(x) - 1:
                rst.append("NO")
        else:
            if ary:
                ary.pop()
                if j == len(x) - 1 and len(ary) == 0:
                    rst.append("YES")
                elif j == len(x) - 1 and len(ary) != 0:
                    rst.append("NO")
            else:
                rst.append("NO")
                break
for i in rst:
    print(i)