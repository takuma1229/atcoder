Sx, Sy, Gx, Gy = map(int, input().split())

for i in range(Gx):
    # x軸への傾き
    kata_to_x = Sy / Gx - i
    # x軸からの傾き
