n = input()
len_n = len(n)

for i in range(5):
  if len(str(n)) == 4:
    print(n)
    exit()
  else:
    n = "0" + n

