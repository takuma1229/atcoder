n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
count = 0

for i in range(n):
  if B[i] >= A[i]:
    B[i] -= A[i]
    count += A[i]
  else: 
    count += B[i]
    B[i] = 0

  if B[i] > 0:
    if B[i] >= A[i+1]:
      # B[i] -= A[i+1]
      count += A[i+1]
    else:
      count += B[i]
      A[i+1] -= B[i]

print(count)