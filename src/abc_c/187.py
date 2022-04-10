n = int(input())
dic = set(input() for i in range(n))

for s in dic:
  if "!" + s in dic:
    print(s)
    exit()

print("satisfiable")

#ユニークなリストではなく、ユニークな辞書を作る。
#辞書でin演算すると計算量がO(1)になる