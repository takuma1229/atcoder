N = int(input())
abc_li = [list(map(int, input().split())) for i in range(N)]

#dp[i][k] = i日めに行動kをして得られる幸福度の最大値
dp = [[0]*3 for i in range(N)]
# print(dp[0][0])
dp[0][0] = abc_li[0][0]
dp[0][1] = abc_li[0][1]
dp[0][2] = abc_li[0][2]

# print(dp)

for i in range(1, N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + abc_li[i][0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + abc_li[i][1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + abc_li[i][2]
    # print(dp)


# print(abc_li)
# print(dp)
print(max(dp[N-1]))
