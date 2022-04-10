n = int(input())
n_s = str(n)
n_li = list(n_s)
fx = 0

for i in range(len(n_li)):
  fx += int(n_li[i])

if n % fx == 0:
  print("Yes")
else:
  print("No")