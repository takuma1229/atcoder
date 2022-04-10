n, k = map(int, input().split())
li = []
card_li = [0] * n

for i in range(k):
  cp_li = list(map(str, input().split()))
  c = cp_li[0]
  p = int(cp_li[1])
  li.append(cp_li)
  if c == "L":
    card_li[p-1] = i
  else:
    card_li[n-p] = i

for i in range(k):
  c = li[i][0]
  p = li[i][1]
  if c == "L":
