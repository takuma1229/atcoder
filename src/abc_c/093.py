li = list(map(int, input().split()))
li_s = sorted(li)

if li_s[0] == li_s[1] == li_s[2]:
    print(0)
    exit()

for i in range(1, 1000):
    if li_s[2] - li_s[0] > 1:
        li_s[0] += 2
    elif li_s[2] - li_s[0] == 1:
        li_s[0] += 1
        li_s[1] += 1

    if li_s[0] == li_s[1] == li_s[2]:
        print(i)
        exit()
    li_s = sorted(li_s)
