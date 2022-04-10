N, K = map(int, input().split())
li = []
ans = K
max_city = K
now = 0

for i in range(N):
    ab_li = list(map(int, input().split()))
    li.append(ab_li)
    max_city += ab_li[1]

li_s = sorted(li)
print(li_s)

for i in range(N):
    if K < li_s[i][0] - ans:
        ans += K
        print(ans)
        print("途中で死にました")
        exit()
    else:
        ans = li_s[i][0]
        K -= li_s[i][0]
        K += li_s[i][1]
        print(str(i) + ":" + str(K))

print(max_city)
