n = int(input())
A = []

for i in range(n):
  ai = int(input())
  A.append(ai)

A_s = sorted(A, reverse=True)

for i in range(n):
  ai = A[i]
  if A_s[0] == ai:
    print(A_s[1])
  else:
    print(A_s[0])