n = int(input())
li = [2,1]

for i in range(2, n+1):
  plus = li[-1] + li[-2]
  li.append(plus)

print(li[-1])
