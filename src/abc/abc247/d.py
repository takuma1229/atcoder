Q = int(input())
cylinder = []

#[i, k] = iと書かれたボールがk個ある
for i in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    cylinder.append([query[1], query[2]])
  else:
    out_ball_num = query[1]
    k = 0
    print_num = 0
    while out_ball_num > 0:
      if cylinder[k][1] < out_ball_num:
        print_num += cylinder[k][1] * cylinder[k][0]
        out_ball_num -= cylinder[k][1]
        del cylinder[0]
      else:
        print_num += cylinder[k][0] * out_ball_num
        print(print_num)
        cylinder[k][1] -= out_ball_num
        out_ball_num = 0
        