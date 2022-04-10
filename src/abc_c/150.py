import itertools as iter

n = int(input())
P = list(map(int, input().split()))
P_t = tuple(P)
Q = list(map(int, input().split()))
Q_t = tuple(Q)

default_li = []
for i in range(1, n+1):
  default_li.append(i)

all_li = list(iter.permutations(default_li))
all_li_s = sorted(all_li)

a = all_li_s.index(P_t)
b = all_li_s.index(Q_t)

print(abs(a-b))