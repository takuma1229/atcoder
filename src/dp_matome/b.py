N, K = map(int, input().split())
h = list(map(int, input().split()))

# dp[i] = iに辿りつくまでの最小コスト
dp = [10**6]*N
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    # とりあえずこれを設定しておき、for-ifの中でminをとる
    dp[i] = dp[i-1] + abs(h[i]-h[i-1])
    for k in range(2, K+1):
        # kがiより大きくならない範囲で処理
        if i-k >= 0:
            dp[i] = min(abs(h[i]-h[i-k])+dp[i-k], dp[i])

print(dp[N-1])
