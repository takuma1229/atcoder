import math

N = int(input())
plan_li = []
ok = True
for i in range(N):
    plan = list(map(int, input().split()))
    plan_li.append(plan)

for i in range(N):
    if i == 0:
        dis = ((plan_li[i][1] ** 2) + (plan_li[i][2] ** 2)) ** 0.5
        time = plan_li[i][0]
        ex_time = (time - math.ceil(dis))
        if ex_time % 2 == 0:
            ok = True
        else:
            ok = False
    else:
        dis = (((plan_li[i][1] - plan_li[i-1][1]) ** 2) +
               ((plan_li[i][2] - plan_li[i-1][2]) ** 2)) ** 0.5
        time = plan_li[i][0] - plan_li[i-1][0]
        ex_time = (time - math.ceil(dis))
        if ex_time % 2 == 0:
            ok = True
        else:
            ok = False
    if not ok:
        print("No")
        exit()


print("Yes")
