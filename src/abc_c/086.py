import math
import numpy as np


def manhattan_distance(point_a, point_b):  # xy座標における二点間のマンハッタン距離を求める
    a = np.array(point_a)
    b = np.array(point_b)
    return(np.linalg.norm(a-b, ord=1))


N = int(input())
plan_li = []
ok = True
for i in range(N):
    plan = list(map(int, input().split()))
    plan_li.append(plan)

for i in range(N):
    if i == 0:
        dis = int(manhattan_distance([plan_li[i][1], plan_li[i][2]], [0, 0]))
        time = plan_li[i][0]
        if time < dis:
            print("No")
            exit()
        ex_time = (time - dis)
        if ex_time % 2 == 0:
            ok = True
        else:
            ok = False
    else:
        dis = manhattan_distance([plan_li[i][1], plan_li[i][2]], [
            plan_li[i-1][1], plan_li[i-1][2]])
        time = plan_li[i][0] - plan_li[i-1][0]
        if time < dis:
            print("No")
            exit()
        ex_time = (time - dis)
        if ex_time % 2 == 0:
            ok = True
        else:
            ok = False
    if not ok:
        print("No")
        exit()


print("Yes")
