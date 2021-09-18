from collections import Counter

n = int(input())
A = list(map(int, input().split()))
c = Counter()

ans = 0
for i in range(n):
  ans += i - c[A[i]]
  c[A[i]] += 1

print(ans)

