n, a, b = map(int, input().split())
ans = 0

for i in range(1, n+1):
  str_i = str(i)
  i_li = str(i)
  i_sum = 0
  for k in range(len(i_li)):
    i_sum += int(i_li[k])
  if a <= i_sum <= b:
    ans += i 

print(ans)