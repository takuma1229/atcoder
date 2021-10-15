n = int(input())
s = input()
s_li = list(s)
ans_li = []

s_li_u = list(set(s_li))
if len(s_li_u) == 1:
  print(0)
  exit()

if s_li.count("W") == 1:
  if s_li[-1] == "W":
    print(0)
    exit()

if s_li.count("E") == 1:
  if s_li[-1] == "E":
    print(0)
    exit()

#wとeに対してそれぞれ累積和的にリストを作っていく
w_cumu_li = [0] * n
e_cumu_li = [0] * n

for i in range(n):
  if i == 0:
    if s_li[i] == "W":
      w_cumu_li[i] += 1
    else:
      e_cumu_li[i] += 1
  else:
    if s_li[i] == "W":
      w_cumu_li[i] = w_cumu_li[i-1] + 1
      e_cumu_li[i] = e_cumu_li[i-1]
    else:
      e_cumu_li[i] = e_cumu_li[i-1] + 1
      w_cumu_li[i] = w_cumu_li[i-1]

for i in range(n):
  if i == 0:
    ans_li.append(e_cumu_li[-1] - e_cumu_li[0])
    continue
  elif i == n-1:
    ans_li.append(w_cumu_li[-1] - w_cumu_li[0])
    continue
  ans_w =  w_cumu_li[i-1]
  ans_e =  e_cumu_li[-1] - e_cumu_li[i]
  ans_li.append(ans_w + ans_e)

print(min(ans_li))