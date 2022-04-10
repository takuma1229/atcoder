n = input()
op_cnt = len(n) - 1

for i in range(2 ** op_cnt):
  op = ["-"] * op_cnt
  for k in range(op_cnt):
    if((i >> k)) & 1:
      op[k] = "+"
  print(op)