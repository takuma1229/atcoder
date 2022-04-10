N, W = map(int, input().split())
li = []
taste_sum = 0

for i in range(N):
    sm_li = list(map(int, input().split()))
    li.append(sm_li)

li_s = sorted(li, reverse=True)

for i in range(N):
    if W >= li_s[i][1]:
        taste_sum += li_s[i][0] * li_s[i][1]
        W -= li_s[i][1]
    else:
        taste_sum += li_s[i][0] * W
        print(taste_sum)
        exit()

print(taste_sum)
# print("over of program")
