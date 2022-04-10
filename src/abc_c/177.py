N = int(input())
A = list(map(int, input().split()))
ans = 0

li = [0] * N
li[0] = A[0]

for i in range(1, N):
    li[i] = li[i-1] + A[i]

for i in range(1, N):
    ans += li[i-1] * A[i]
    ans %= (10 ** 9 + 7)

print(ans)
