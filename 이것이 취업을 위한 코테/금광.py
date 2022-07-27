answer = []

for t in range(int(input())):
    n, m = map(int, input().split())
    ary = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(ary[index:index + m])
        index += m

    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위면 더 위가 없어서 0
            if i == 0:
                left_w = 0
            else:
                left_w = dp[i-1][j-1]
            
            left = dp[i][j-1]

            # 왼쪽 아래면 더 아래가 없어서 0
            if i == n-1:
                left_s = 0
            else:
                left_s = dp[i+1][j-1]

            dp[i][j] = dp[i][j] + max(left_w, left, left_s)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    
    answer.append(result)

for i in answer:
    print(i)

