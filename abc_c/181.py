n = int(input())
li = []
for i in range(n):
  li_s = list(map(int, input().split()))
  li.append(li_s)

for i in range(n):
  for k in range(i):
    for p in range(k):
      if (li[i][0] - li[k][0]) != 0 and (li[i][0] - li[p][0]) != 0:
        tilt1 = (li[i][1] - li[k][1]) / (li[i][0] - li[k][0])
        tilt2 = (li[i][1] - li[p][1]) / (li[i][0] - li[p][0])
        if tilt1 == tilt2:
          print("Yes")
          exit()
      elif li[i][0] == li[k][0] == li[p][0] or li[i][1] == li[k][1] == li[p][1]:
        print("Yes")
        exit()
      

print("No")
