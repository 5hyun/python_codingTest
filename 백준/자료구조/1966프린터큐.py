from collections import deque
t = int(input())
rst = []
for i in range(t):
    ary = deque()
    n, m = map(int, input().split())
    x = input().split()
    for j in range(n):
        ary.append([])
        ary[j].append(int(x[j]))
        ary[j].append(j)
    sam = ary[m][1]#찾으려는 값의 처음 순서
    count = 1
    while(True):
        a = max(ary)[0]#현재의 최고 우선순위 값
        if a == ary[0][0] and ary[0][1] == m:
            rst.append(count)
            break
        elif a == ary[0][0] and ary[0][1] != m:
            ary.popleft()
            count += 1
        elif a == ary[0][0]:
            if max(ary)[1] == m:
                rst.append(count)
                break
            ary.popleft()
            count += 1
        else:
            tmp = ary.popleft()
            ary.append(tmp)
for i in rst:
    print(i)