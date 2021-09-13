import math

a, b, h, m = map(int, input().split())

hour_do = 30 * h + (0.5 * m) #時間の針は分刻みでも少しずつ進んでいくことに注意
min_do = 6 * m
angle = abs(hour_do - min_do)
if angle >= 180:
  angle = 360 - angle
cos = math.cos(math.radians(angle))
ans2 = a**2 + b**2 - 2*a*b*cos
ans = ans2 ** 0.5
print(ans)