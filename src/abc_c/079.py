n = input()
n_li = list(n)
op_cnt = len(n) - 1
op_li = []

for i in range(2 ** op_cnt):
  op = ["-"] * op_cnt
  for k in range(op_cnt):
    if((i >> k)) & 1:
      op[k] = "+"
  op_li.append(op)


for i in range(len(op_li)):
  formula = n_li[0] + op_li[i][0] + n_li[1] + op_li[i][1] + n_li[2] + op_li[i][2] + n_li[3]
  if eval(formula) == 7:
    print(formula + "=7")
    exit()