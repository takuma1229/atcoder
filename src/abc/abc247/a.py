S = list(input())
ans = ""
for i in range(len(S)):
  if i == 0:
    ans = ans + "0"
    continue
  if S[i-1] == "1":
    ans = ans + "1"
  else:
    ans = ans + "0"

print(ans)