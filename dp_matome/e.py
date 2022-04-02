N, W = map(int, input().split())
w = []
v = []
for i in range(N):
    wt, vt = map(int, input().split())
    w.append(wt)
    v.append(vt)

# dp[i][j] = i個まで入れて良くて、かつ重さj以下のときの最大価値
dp = [[0]*(W+1) for i in range(N+1)]
for i in range(1, N+1):
    for j in range(1, W+1):
        if j - w[i-1] <= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-w[i-1]] + v[i-1])
        dp[i][j] = max(dp[i][j], dp[i-1][j])

print(dp[N][W])
