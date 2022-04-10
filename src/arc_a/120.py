N = int(input())
A = list(map(int, input().split()))
ans = 0

maximum_value = max(A)

for i in range(N):
    A[i] += maximum_value
    if A[i] > maximum_value:
        maximum_value = A[i]
    if not i == N-1:
        print()

A_sum = sum(A)


print(A_sum)
