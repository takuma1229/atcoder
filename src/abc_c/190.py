n, m = map(int, input().split())
li = []
future_li = []
dish = [0] * n
count = 0

for i in range(m):
  ab_li = list(map(int, input().split()))
  li.append(ab_li)
  
k = int(input())
for i in range(k):
  cd_li = list(map(int, input().split()))
  future_li.append(cd_li)

for i in range(k):
  c = future_li[i][0]
  d = future_li[i][1]
  if dish[c-1] == 0 and dish[d-1] == 0:
    c_future = future_li.count(c)
    d_future = future_li.count(d)
    c_need = li.count(c)
    d_need = li.count(d)
    
# for i in range(m):
#   a = li[i][0]
#   b = li[i][1]
#   if dish[a-1] > 0 and dish[b-1] > 0:
#     count += 1

# print(count)