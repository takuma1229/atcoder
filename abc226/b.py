N = int(input())
li = []

for i in range(N):
    sm_li = list(map(int, input().split()))
    li.append(sm_li)

li_t = list(map(tuple, li))

li_u = set(list(li_t))

print(len(li_u))
