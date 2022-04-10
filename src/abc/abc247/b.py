from re import L


N = int(input())
S = []
T = []
name = []
flag = False
dp1 = [False] * N
dp2 = [False] * N
for i in range(N):
  n = list(map(str, input().split()))
  name.append(n)

for i in range(N):
  first = name[i][0]
  second = name[i][1]
  for k in range(N):
    if k == i:
      continue
    if first == name[k][0] or first == name[k][1]:
      dp1[i] = True
    if second == name[k][0] or second == name[k][1]:
      dp2[i] = True

for i in range(N):
  if dp1[i] and dp2[i]:
    print("No")
    exit()

print("Yes")