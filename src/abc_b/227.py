N = int(input())
S = list(map(int, input().split()))
ans = 0

for i in range(N):
    flag = False
    for a in range(1, 253):
        for b in range(1, 253):
            if (4*a*b) + (3*a) + (3*b) == S[i]:
                flag = True
    if not flag:
        ans += 1

print(ans)
