N, K = map(int, input().split())
p = list(map(int, input().split()))
ans_li = []

if N == 1:
    print((p[0] + 1) / 2)
    exit()

for i in range(N):
    p[i] += 1
    p[i] /= 2

cum_li = [0] * N
cum_li[0] = p[0]


for i in range(1, N):
    cum_li[i] = cum_li[i-1] + p[i]

if N == K:
    print(max(cum_li))
    exit()

for i in range(K, N):
    ans = cum_li[i] - cum_li[i-K]
    ans_li.append(ans)


print(max(ans_li))
