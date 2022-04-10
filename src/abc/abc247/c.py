N = int(input())
dp = [[] for i in range(N)]
dp[0] = "1"


for i in range(1,N):
  dp[i] = dp[i-1] + f" {i+1} " + dp[i-1]

print(dp[N-1])