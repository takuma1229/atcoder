n = int(input())
li = []
count = 0

for i in range(n):
  t, l, r = map(int, input().split())
  li_sm = []
  if t == 1:
    for k in range(10 * l, 10 * (r+1)):
      li_sm.append(k)
  elif t == 2:
    for k in range(10 * l, 10 * (r)):
      li_sm.append(k)
  elif t == 3:
    for k in range(10 * (l+1), 10 * (r+1)):
      li_sm.append(k)
  else:
    for k in range(10 * (l+1), 10 * r):
      li_sm.append(k)
  li.append(li_sm)

for i in range(1, n):
  for k in range(i):
    if set(li[i]) & set(li[k]):
      count += 1
      print(str(i) +  "and" + str(k))

print(count)
print(li)