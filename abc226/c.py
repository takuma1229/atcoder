N = int(input())
skill_time_li = [0] * N
li = []
aquire_li = []
count = 0

# 累積和的に必要な時間を記録しておく

for i in range(N):
    sm_li = list(map(int, input().split()))
    need_time = sm_li[0]
    if i != 0:
        for k in range(sm_li[1]):
            need_skill_num = sm_li[k+2]
            need_time += skill_time_li[need_skill_num-1]
    skill_time_li[i] += need_time
    li.append(sm_li)

ans = li[N-1][0]

for i in range(li[N-1][1]):
    need_skill_num_2 = li[N-1][i+2]
    for k in range(li[need_skill_num_2-1][1]):
        need_skill_num_3 = li[need_skill_num_2-1][k+2]
        ans += li[need_skill_num_2 - 1][0]
        if aquire_li.count(need_skill_num_3) <= 0:
            ans += li[need_skill_num_3-1][0]
            aquire_li.append(need_skill_num_3)


print(skill_time_li)

print(skill_time_li[N-1])

print(ans)


# for i in range(li[N-1][1]):
#     last_need_skill_num = li[N-1][i+2]
#     count += skill_time_li[last_need_skill_num]

# count += li[N-1][0]

# print(count)
