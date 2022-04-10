n = int(input())
A = list(map(int, input().split()))
x = int(input())
sum_A = sum(A)

num = x // sum_A
amari = x % sum_A

for i in range(n):
  amari -= A[i]
  if amari < 0:
    tasubeki = i+1
    break

print((n * num) + tasubeki)
