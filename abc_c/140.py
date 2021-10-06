n = int(input())
B = list(map(int, input().split()))
ans_li = []

for i in range(n):
  if i == 0:
    ans_li.append(B[i])
  elif i == n-1:
    ans_li.append(B[n-1-1])
  else:
    Ai = min(B[i], B[i-1])
    ans_li.append(Ai)
  

print(sum(ans_li))