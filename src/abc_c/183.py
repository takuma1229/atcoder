import itertools

n, K = map(int, input().split())
li = []
city_li = []
count = 0

for i in range(n):
    sm_li = list(map(int, input().split()))
    li.append(sm_li)

for i in range(n):
    city_li.append(i)

all_city_route = list(itertools.permutations(city_li))

for i in range(len(all_city_route)):
    time_sum = 0
    if all_city_route[i][0] == 0:
        for k in range(n):
            if k == n-1:
                dep = all_city_route[i][k]
                des = 0
                time_sum += li[dep][des]
                continue
            dep = all_city_route[i][k]
            des = all_city_route[i][k+1]
            time_sum += li[dep][des]
    if time_sum == K:
        count += 1

print(count)
