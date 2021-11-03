N = int(input())
n_li = [0] * N
for i in range(N-1):
    a, b = map(int, input().split())
    n_li[a-1] += 1
    n_li[b-1] += 1

for i in range(N):
    if n_li[i] == 0:
        print("No")
        exit()

if max(n_li) != N-1:
    print("No")
    exit()

print("Yes")
