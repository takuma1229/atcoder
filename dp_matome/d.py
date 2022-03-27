N, W = map(int, input().split())
w = []
v = []
for i in range(N):
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)

# dp[i][j]=iコまで&重さj以下の最大価値
dp = [[0] * (W+1) for i in range(N+1)]
for i in range(1, N+1):
    for j in range(1, W+1):
        # 入れる場合
        if j - w[i-1] >= 0:
            dp[i][j] = max(dp[i-1][j-w[i-1]] + v[i-1], dp[i][j])
        # 入れない場合
        dp[i][j] = max(dp[i-1][j], dp[i][j])

print(dp[N][W])
