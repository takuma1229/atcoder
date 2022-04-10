import itertools as iter

n = input()
n_li = list(n)

print(list(iter.permutations(n_li)))
# 引数にリストを渡して、そこからさらにリストを生成するモジュール。
