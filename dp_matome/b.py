N, K = map(int, input().split())
h = list(map(int, input().split()))

# dp[i] = iに辿りつくまでの最小コスト
dp = [0]*N
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    cost_list = []
    for k in range(1, max(i, K+1)):
        cost = abs(h[i]-h[i-k])+dp[i-k]
        cost_list.append(cost)
    dp[i] = min(cost_list)

print(dp[N-1])
print(dp)
