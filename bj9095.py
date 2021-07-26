T = int(input())

for i in range(1, T+1):
    n = int(input())
    dp = [1, 2, 4]
    for j in range(3, n):
        sum=dp[j-1]+dp[j-2]+dp[j-3]
        dp.append(sum)
    print(dp[n-1])
