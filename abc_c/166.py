N, M = map(int, input().split())
H = list(map(int, input().split()))
li = [-1] * N
count = 0

for i in range(M):
    sm_li = list(map(int, input().split()))
    a = sm_li[0]
    b = sm_li[1]
    li[a-1] = max(li[a-1], H[b-1])
    li[b-1] = max(li[b-1], H[a-1])

for i in range(N):
    if li[i] == -1:
        count += 1
        continue

    if li[i] < H[i]:
        count += 1

print(count)
