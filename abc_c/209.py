N = int(input())
C = list(map(int, input().split()))
ans = 1

C_s = sorted(C)

for i in range(N):
    ans = ans * (C_s[i] - i) % 1000000007

print(ans)
