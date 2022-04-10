import collections

n = int(input())
A = list(map(int, input().split()))
a_count = collections.Counter(A)

ans = n*(n-1) // 2
for i in a_count.values():
  ans -= i*(i-1)//2

print(ans)