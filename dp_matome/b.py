N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [10**10] * N
dp[0] = 0
dp[1] = abs(h[1]-h[0])

for i in range(2, N):
    smallest_list = []
    for k in range(1, K+1):
        smallest = abs(h[i]-h[i-k])+dp[i-k]
        smallest_list.append(smallest)
    dp[i] = min(smallest_list)

print(dp[N-1])
