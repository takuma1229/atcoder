x, k, d = map(int, input().split())
first = abs(x) % d 
if d * k < abs(x):
  print(abs(x) - (d * k))
  exit()
if x < 0:
  first = first * -1
first_num = abs(x) // d
remain = k - first_num
if remain % 2 == 0:
  print(abs(first))
else:
  print(abs(abs(first) - d))
