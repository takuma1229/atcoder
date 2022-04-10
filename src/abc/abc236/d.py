import itertools as iter
import numpy as np
from operator import xor
import string

alpha = string.ascii_lowercase
alpha_li = list(alpha)

N = int(input())

A = []
satis_li = []

for i in range(2*N-1):
    sm_li = list(map(int, input().split()))
    for satis in sm_li:
        satis_li.append(satis)
    A.append(sm_li)

full_list = list(iter.permutations(satis_li))
xor_li = []

# print(len(full_list))

for i in range(len(full_list)):
    li = list(full_list[i])
    # print(li)
    xor = li[0]
    xor_li.append(li[0])
    if len(li) == 1:
        continue
    for k in range(1, len(li)):
        xor = xor ^ li[k]
        # print(xor)
        xor_li.append(xor)
    # print("==================")
# print(xor_li)
print(max(xor_li))
