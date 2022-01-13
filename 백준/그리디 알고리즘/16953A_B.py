'''
a, b = map(int, input().split())
count = 0

while(b >= 1):
    if(b%2 != 0):
        b -= 1
        b = b / 10
        count += 1
        if(b == a):
            print(count + 1)
            break
    elif(b %2 == 0):
        b = b / 2
        count += 1
        if(b == a):
            print(count + 1)
            break
else:
    print(-1)
'''
from collections import deque 

a, b = map(int, input().split()) 
res = -1 
que = deque([(a, 1)])#a가 2면, 덱에 2와 1이 있다.
while que:
    i, cnt = que.popleft() #왼쪽 값을 빼고싶으면 popleft()
    if i == b:
        res = cnt 
        break
    
    if i*2 <= b: #2로 곱하는 경우
        que.append((i*2, cnt+1))
    if int(str(i)+'1') <= b: #뒤에 1을 추가하는 경우
        que.append((int(str(i)+'1'), cnt+1)) 
print(res)