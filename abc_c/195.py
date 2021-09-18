n = int(input())
n_li = list(str(n))
length = len(n_li)
times = 0
already = 0

if length < 4:
  print(0)
  exit()
elif length < 7: #コンマ一回ずつの場合
  print(n - (999))
  exit()
elif length < 10: #コンマ2回ずつの場合
  times =(n - 999999)
  already = 999999 - 999
  print(times * 2 + already)
  exit()
elif length < 13: #コンマ3回ずつの場合
  times = (n - 999999999)
  already1 = (999999 - 999) 
  already2 = (999999999 - 999999)
  print((times * 3) + (already1) + (already2 * 2))
  exit()
elif length < 16: #コンマ4回ずつの場合
  times = (n - 999999999999)
  already1 = (999999 - 999)
  already2 = (999999999 - 999999)
  already3 = (999999999999 - 999999999)
  times = (n - 999999999999)
  print((times * 4) + (already3 * 3) + (already2 * 2) + (already1))
  exit()
else: #n=10 ** 15の場合
  already1 = (999999 - 999)
  already2 = (999999999 - 999999)
  already3 = (999999999999 - 999999999)
  already4 = (999999999999999 - 999999999999)
  print((already4 * 4) + (already3 * 3) + (already2 * 2) + (already1) + 5)
  exit()