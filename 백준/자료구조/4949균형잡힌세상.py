x = 1
lst = []
while(True):
    x = input()
    if x == '.':
        break
    lst.append(x)
rst = []
for i in range(len(lst)):
    ary = []   
    for j in range(len(lst[i])):
        if lst[i][j] == '(' or lst[i][j] == '[':
            ary.append(lst[i][j])
        elif lst[i][j] == ')' or lst[i][j] == ']':
            if len(ary) == 0:
                rst.append("no")
                break
            if (lst[i][j] == ')' and ary[-1] == '(') or ((lst[i][j] == ']' and ary[-1] == '[')):
                ary.pop()
            else:
                rst.append("no")
                break
        if j == len(lst[i]) - 1 and ary:
            rst.append("no")
        elif j == len(lst[i]) - 1 and len(ary) == 0:
            rst.append("yes")
for i in rst:
    print(i)