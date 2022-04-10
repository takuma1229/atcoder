N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
B_Cn_li = []
count_x = [0] * N
count_A = [0] * N
ans = 0

for j in range(N):
    B_Cj = B[C[j]-1] - 1
    count_x[B_Cj] += 1

for i in range(N):
    A_i = A[i] - 1
    count_A[A_i] += 1

for i in range(N):
    ans += count_x[i] * count_A[i]

print(ans)
