N, W = map(int, input().split())
weight_list = []
value_list = []
for i in range(N):
    w, v = map(int, input().split())
    weight_list.append(w)
    value_list.append(v)

# dp[i][k] = i番目の荷物まで検討して、重さk以下での価値の最大値
dp = [[0]*(W+1) for i in range(N+1)]

for i in range(1, N+1):
    for k in range(1, W+1):
        # 入れたときの処理
        if k - weight_list[i-1] >= 0:
            dp[i][k] = max(dp[i][k], dp[i-1]
                           [k-weight_list[i-1]] + value_list[i-1])
        # 入れていようと入れてなかろうと、この処理は行う必要がある（入れてもdp[i-1）[k]のほうが大きくなるパターンがある)
        dp[i][k] = max(dp[i][k], dp[i-1][k])

print(dp[N][W])
