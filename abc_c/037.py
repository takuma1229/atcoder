n, k = map(int, input().split())
a = list(map(int, input().split()))
sum_li = []

c = [0] * n

c[0] = a[0]

for i in range(1,n):
  c[i] = c[i-1] + a[i]

for i in range(k-1, n):
  if i == k-1:
    sum_li.append(c[i])
  else:
    sum_li.append(c[i] - c[i-k])

print(sum(sum_li))
