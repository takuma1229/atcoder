N = int(input())
A = list(map(int, input().split()))
ans_li = []
ans = 0

for i in range(N):
    x = A[i]
    for k in range(i, N):
        x = min(x, A[k])
        ans = max(ans, (k - i + 1) * x)


print(ans)
