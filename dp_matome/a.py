N = int(input())
h = list(map(int, input().split()))

dp = [0] * N

dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    # i を現在いる足場と考える。
    # i 番目の足場へ行く方法として i-i 番目からのジャンプと i-2 番目からのジャンプがある
    # 2 通りの行き方のうちコストの少ない方を dp[i] とする
    dp[i] = min(dp[i-2] + abs(h[i] - h[i-2]), dp[i-1] + abs(h[i] - h[i-1]))

print(dp[-1])
