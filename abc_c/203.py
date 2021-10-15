n, k = map(int, input().split())
li = []
ans = 0

for i in range(n):
  li_ab = list(map(int, input().split()))
  li.append(li_ab)

li_s = sorted(li)

for i in range(n):
  if k < li_s[i][0]:
    if i == n-1:
      ans += k
    else:
      if li_s[i][0] != li_s[i+1][0]:
        ans += k
        print(ans)
        exit()
      else:
        k -= (li_s[i][0] - li_s[i-1][0])
        k += li_s[i][1]
        ans = li_s[i][0]
  else:
    if i == 0:
      k -= li_s[i][0]
      k += li_s[i][1]
      ans = li_s[i][0]
    else:
      k -= (li_s[i][0] - li_s[i-1][0])
      k += li_s[i][1]
      ans = li_s[i][0]

print(ans + k)
  