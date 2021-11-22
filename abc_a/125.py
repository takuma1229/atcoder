A, B, T = map(int, input().split())
ans = 0
if A > T:
    print(0)
    exit()
for i in range(1, 21):
    ans += B
    if (i+1) * A > T:
        print(ans)
        exit()
