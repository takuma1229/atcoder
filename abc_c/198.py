r, x, y = map(int, input().split())
step = 0
if 

dis = ((x ** 2) + (y ** 2)) ** 0.5

for i in range(10 ** 5):
  if dis > 2*r :
    step += 1
    dis -= 2 * r
  else:
    step += 2
    print(step)
    exit()