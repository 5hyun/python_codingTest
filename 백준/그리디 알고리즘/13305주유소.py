n = int(input())
d = input().split()
d = list(map(int, list(d)))
city = input().split()
city = list(map(int, list(city))) 
won = 0
won = city[0] * d[0]
min = city[0]
for i in range(1, n-1):
    if(min > city[i]):
        min = city[i]
    won += min * d[i]
print(won)