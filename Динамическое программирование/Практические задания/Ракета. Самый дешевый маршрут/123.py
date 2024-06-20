def knapsack(values, weights, W):
    n = len(values)
    dp = [[0] * (W + 1) for i in range(n + 1)]
    # item = [[0] * (W + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp


if __name__ == 'main':
    values = [120, 100, 150]
    weights = [1, 2, 3]
    W = 5
    print(knapsack(values, weights, W))
