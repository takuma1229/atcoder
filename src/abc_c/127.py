n, m = map(int, input().split())
l_li = []
r_li = []

for i in range(m):
  l, r = map(int, input().split())
  l_li.append(l)
  r_li.append(r)
  

l_max = max(l_li)
r_min = min(r_li)

if r_min - l_max < 0:
  print(0)
else:
  print(r_min - l_max + 1)