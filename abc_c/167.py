N, M, X = map(int, input().split())
li = []

ans_li = []

for i in range(N):
    sm_li = list(map(int, input().split()))
    li.append(sm_li)

for i in range(2 ** N):
    bag = []
    skill_li = [0] * M  # ここで設定しておかないとforが回っても保持されている！
    total = 0
    for j in range(N):
        if ((i >> j) & 1):
            for p in range(1, M+1):
                skill_li[p-1] += li[j][p]
            total += li[j][0]  # ここに書かないとskillの値見るたびに加算されてしまう！
    ok = True
    for skill_num in range(M):
        if skill_li[skill_num] < X:
            ok = False
    if ok:
        ans_li.append(total)
if len(ans_li) == 0:
    print(-1)
    exit()
print(min(ans_li))
