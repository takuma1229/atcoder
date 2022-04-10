s = input()
s_li = list(s)
s_len = len(s_li)

if s_len == 1 or s_len == 0:
  print(0)
  exit()

one_count = s_li.count("1")
zero_count = s_li.count("0")

print(min(one_count, zero_count) * 2)