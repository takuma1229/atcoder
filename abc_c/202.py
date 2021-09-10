n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
count = 0

for i in range(n):
  for j in range(n):
    if A[i] == B[C[j]-1]:
      count += 1

print(count)
#TLE