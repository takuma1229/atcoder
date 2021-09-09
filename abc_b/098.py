n = int(input())
s = input()
ans_li = []

for i in range(n):
  s_f = s[:i]
  s_l = s[i:n]
  li = []
  for k in range(min(len(s_f), len(s_l))):
    l = s_f[k]
    if s_l.count(l) != 0:
      li.append(l)
  li_u = list(set(li))
  ans_li.append(len(li_u))
  
print(max(ans_li))
