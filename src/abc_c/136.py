n = int(input())
H = list(map(int, input().split()))

for i in range(n):
  if i == 0:
    H[i] -= 1
  else:
    if H[i] > H[i-1]:
      H[i] -= 1
    elif H[i] == H[i-1]:
      continue
    else:
      print("No")
      exit()
    
print("Yes")