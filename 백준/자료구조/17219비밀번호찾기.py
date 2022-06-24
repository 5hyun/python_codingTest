n, m = map(int, input().split())
dic = {}

for i in range(n):
    site, password = map(str, input().split())
    dic[site] = password

answer = []

for i in range(m):
    x = input()
    answer.append(dic[x])

for i in answer:
    print(i)