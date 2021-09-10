n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
bcj = [0] * n

for f in range(n):
  tmp = B[C[j]-1]
  bcj.append(tmp)

  a = collections.Counter(A)

  ans = 0
  for i in range(len(bcj)):
    ans += a[bcj[i]]

print(ans)