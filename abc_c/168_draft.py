import math

a, b, h, m = map(int, input().split())
#余弦定理か何か使う問題か？
if h == 0 or h == 12:
  hour_do = 0
  min_do = 360 / m
  angle = abs(hour_do - min_do)
  cos = math.cos(angle)
  ans = (a**2 + b**2 - 2*a*b*cos) ** 0.5
  print(ans) 
  exit()
elif m == 0:
  if h < 12:
    hour_do = 360 / 12 * h
  else:
    hour_do = 360 / 12 * h
  min_do = 0
  angle = abs(hour_do - min_do)
  cos = math.cos(angle)
  ans = (a**2 + b**2 - 2*a*b*cos) ** 0.5
  print(ans)
  exit()

if h < 12:
  hour_do = 360 / 12 *h
  min_do = 360 / 60 * m
  angle = abs(hour_do - min_do)
  cos = math.cos(angle)
  ans = (a**2 + b**2 - 2*a*b*cos) ** 0.5
else:
  hour_do = 360 / 12 * h
  min_do = 360 / 60 * m
  angle = abs(hour_do - min_do)
  cos = math.cos(angle)
  ans = (a**2 + b**2 - 2*a*b*cos) ** 0.5

  print(ans)
