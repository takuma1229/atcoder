n, m = map(int, input().split())
on_off_li = []
k_s_li = []

ok_count = 0

for i in range(m):
  k_s = list(map(int, input().split()))
  k_s_li.append(k_s)

p = list(map(int, input().split()))

for i in range(2 ** n):
  switch_li = ["off"] * n
  for j in range(n):
    if ((i >> j) & 1):
      switch_li[j] = "on"
  on_off_li.append(switch_li)

for i in range(len(on_off_li)):
  ok = True
  for j in range(m):
    on_switch = 0
    for k in range(k_s_li[j][0]):
      switch_num = k_s_li[j][k+1]
      if on_off_li[i][switch_num-1] == "on":
        on_switch += 1
    if not on_switch % 2 == p[j]:
      ok = False
  if ok:
    ok_count += 1

print(ok_count)
