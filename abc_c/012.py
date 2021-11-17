N = int(input())
kuku_li = []
ans_li = []

for i in range(1, 10):
    for k in range(1, 10):
        kuku_li.append(i*k)

kuku_sum = sum(kuku_li)

for i in range(1, 10):
    for k in range(1, 10):
        if N + (i * k) == kuku_sum:
            ans_li.append([i, k])

ans_li = sorted(ans_li)

for i in range(len(ans_li)):
    print(str(ans_li[i][0]) + " x " + str(ans_li[i][1]))
