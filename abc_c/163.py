n = int(input())
A = list(map(int, input().split()))
li = [0] * n

for i in range(n-1):
  li[A[i]-1] += 1

for i in range(n):
  print(li[i])