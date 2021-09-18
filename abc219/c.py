x = input()
x_li = list(x)
n = int(input())
name_li = []
num_name_li = []

for i in range(n):
  name = input()
  name_li = list(name)
  num_li = []
  for k in range(len(name_li)):
    number = x_li.index(name_li[k])
    num_li.append(str(number))
  num_name = "".join(num_li)
  num_name_li.append(str(num_name))

num_name_s = sorted(num_name_li)

for i in range(len(num_name_s)):
  num_name_last_li = list(num_name_s[i])
  letter_name = []
  for k in range(len(num_name_last_li)):
    letter_name.append(x_li[int(num_name_last_li[k])])
  print("".join(letter_name))

#わからない！！！！！！