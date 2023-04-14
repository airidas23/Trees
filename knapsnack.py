def knapsack(W, n, w):
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            dp[i][j] = dp[i-1][j]
            if j >= w[i-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-w[i-1]] + w[i-1])
    return dp[n][W]

W, n = map(int, input().split())
w = list(map(int, input().split()))
print(knapsack(W, n, w))
