x = input()
x = x.replace('()', '1')
ary = []
sum = 0
for i in range(len(x)):
    if x[i] == '1' and len(ary) == 0:
        continue
    elif x[i] == '1':
        for j in range(len(ary)):
            ary[j] += 1
    elif x[i] == '(':
        ary.append(0)
    elif x[i] == ')':
       sum += ary[-1]+1
       ary.pop()
print(sum) 