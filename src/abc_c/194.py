N = int(input())
A = list(map(int, input().split()))
ans = 0

li = [0] * 401

for i in range(N):
    li[A[i]+200] += 1

for i in range(1, 401):
    for k in range(i):
        diff = abs((i-200) - (k-200))
        ans += (diff ** 2) * li[i] * li[k]

print(ans)
