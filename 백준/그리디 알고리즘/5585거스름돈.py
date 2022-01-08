x = int(input())
c = 1000-x
sum = 0

sum += c // 500
c %= 500
sum += c // 100
c %= 100
sum += c // 50
c %= 50
sum += c // 10
c %= 10
sum += c // 5
c %= 5
sum += c // 1
c %= 1
 
print(sum)