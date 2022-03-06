N = int(input())
h = list(map(int, input().split()))

# dp[i] = iにたどり着くまでの最小コスト
dp = [0] * (10**6)

dp[0] = 0
dp[1] = abs(h[1]-h[0])

for i in range(2, N):
    one = dp[i-1] + abs(h[i]-h[i-1])
    two = dp[i-2] + abs(h[i]-h[i-2])
    dp[i] = min(one, two)

print(dp[N-1])
