n, m, k = map(int, input().split()) 
#N은 몇개 입력 개수, M은 숫자가 더해지는 횟수, K는 연속해서 K번까지만 더할 수 있다.
data = list(map(int, input().split()))

data.sort() 
first = data[n - 1] 
second = data[n - 2]

count = int(m / (k + 1)) * k
#k번까지만 연속하게 할 수 있으니 가장 큰 수가 K번 더해지고 두번째로 큰수가 더해진다. 따라서 K+1번까지가 하나의 수열이 된다. 
#그러면 M // (K+1)에다가 K를 곱하면 (M // (K+1)) * K가 가장 큰 수가 더해지는 횟수
count += m % (k + 1)
# 한번에 나눠떨어지지 않으면 (M // (K+1)) * K에다가 M을 K+1로 나눈 나머지만큼 더해줘야 가장 큰 수가 더해지는 횟수

result = 0
result += (count) * first 
result += (m - count) * second 

print(result) 