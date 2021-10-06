import itertools as iter

n = input()
n_li = list(n)

all_li = list(iter.permutations(n_li))

ab_li = []

for i in range(len(all_li)):
  for k in range(1,len(n)):
    a_li = all_li[i][:k]
    a = "".join(a_li)
    b_li = all_li[i][k:]
    b = "".join(b_li)
    ab = int(a) * int(b)
    ab_li.append(ab)

print(max(ab_li))