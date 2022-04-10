n, m = map(int, input().split())
li = []
ans = 0

for i in range(n):
  ab = list(map(int, input().split()))
  li.append(ab)

li_s = sorted(li)

for i in range(n):
  if m > li_s[i][1]:
    ans += li_s[i][0] * li_s[i][1]
    m -= li_s[i][1]
  else:
    ans += li_s[i][0] * m
    print(ans)
    exit()