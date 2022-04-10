n = int(input())
li = []
b_li = []
second = 0
a_li = []
need_s_li = []
ans = 0

for i in range(n):
    ab_li = list(map(int, input().split()))
    a = ab_li[0]
    b = ab_li[1]
    a_li.append(a)
    b_li.append(b)
    li.append(ab_li)
    second += a / b
    need_s = a / b
    need_s_li.append(need_s)

second = second / 2

for i in range(n):
    if second - need_s_li[i] >= 0:
        ans += a_li[i]
        second -= need_s_li[i]
    else:
        ans += b_li[i] * second

print(ans)
