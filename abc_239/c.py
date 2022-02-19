x1, y1, x2, y2 = map(int, input().split())
flag = True

first_dis = ((x1-x2)**2 + (y1-y2)**2)**0.5
if first_dis > 2 * (5**0.5):
    print("No")
    exit()

# 一個目の点について
for a in range(x1-100, x1+100):
    for b in range(y1-100, y1+100):
        dis1 = ((a-x1)**2 + (b-y1)**2)**0.5
        dis2 = ((a-x2)**2 + (b-y2)**2)**0.5
        if dis1 == dis2 and dis1 == 5**0.5:
            print("Yes")
            exit()

print("No")
exit()
