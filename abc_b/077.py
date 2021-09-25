n = input()
length = len(n)
if length % 2 != 0:
  length += 1
li = []


for i in range(10 ** (length // 2)):
  if i ** 2 <= int(n):
    li.append(i**2)

print(max(li))