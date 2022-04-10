s = input()
s_li = list(s)
s_len = len(s)

li_0 = []
li_1 = []

count1 = 0
count2 = 0

for i in range(s_len):
  if i % 2 == 0:
    li_0.append(0)
  else:
    li_0.append(1)

for i in range(s_len):
  if i % 2 == 0:
    li_1.append(1)
  else:
    li_1.append(0)

for i in range(s_len):
  if int(s_li[i]) != li_0[i]:
    count1 += 1


for i in range(s_len):
  if int(s_li[i]) != li_1[i]:
    count2 += 1

print(min(count1, count2))