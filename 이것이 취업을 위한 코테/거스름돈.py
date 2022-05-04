n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:#이렇게 하면 코드의 시간 복잡도는 O(K)이다. 
#이 알고리즘은 동전의 종류(coin_types)에만 영향을 받고 거슬러 줘야하는 금액의 크기와는 무관하다.
    count += n // coin
    n %= coin

print(count)