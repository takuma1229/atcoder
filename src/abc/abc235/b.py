N = int(input())
H = list(map(int, input().split()))

for i in range(N):
    if i == N-1:
        print(H[i])
        exit()
    if H[i+1] > H[i]:
        continue
    else:
        print(H[i])
        exit()
