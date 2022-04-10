H, W = map(int, input().split())
li = []
smallest = 10000000
ans = 0

for i in range(H):
    sm_li = list(map(int, input().split()))
    smallest = min(smallest, min(sm_li))
    li.append(sm_li)

for i in range(H):
    for k in range(W):
        ans += li[i][k] - smallest

print(ans)
