

N, K, X = map(int, input().split())
A = list(map(int, input().split()))
# A = sorted(A, reverse=True)

for i in range(N):
    max_use_num = A[i] // X
    if max_use_num <= K:
        # A[i] = A[i] - (X * max_use_num)
        A[i] = A[i] % X
        K -= max_use_num
        # print(f"A[{i}] == {A[i]}")
    else:
        A[i] = A[i] - (X * max_use_num)
        print(sum(A))
        exit()

A_new = sorted(A, reverse=True)
for i in range(N):
    if K > 0:
        A_new[i] = 0
        K -= 1
    elif K == 0:
        print(sum(A_new))
        exit()

print(sum(A_new))
