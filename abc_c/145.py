#最大距離を通るパターンと通らないパターンで距離合計が変わってくる。
n = int(input())
li = []
dis_li = []

for i in range(n):
  li.append(list(map(i nt, input().split())))

for i in range(n):
  dis = 0
  for k in range(i):
    dis_li.append((((li[i][0] - li[k][0])**2) + ((li[i][1] - li[k][1])**2)) ** 0.5)

max_dis = max(dis_li)
min_dis = min(dis_li)

big_ave = 