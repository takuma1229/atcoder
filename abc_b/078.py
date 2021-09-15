x,y,z = map(int, input().split())

for i in range(x):
  if y * i + (z * (i+1)) <= x:
    continue
  else:
    print(i-1)
    exit()

