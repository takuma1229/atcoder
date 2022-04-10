N = int(input())
k = len(str(N))
ans_li = []

if N % 3 == 0:
    print(0)
    exit()

N_li = list(str(N))

for i in range(1, k):
    for j in range(k):
        new_li = list(str(N))
        try:
            del new_li[j:j+i]
        except:
            del new_li[j]
        sum_num = 0
        for p in range(len(new_li)):
            sum_num += int(new_li[p])
        if sum_num % 3 == 0:
            ans_li.append(i)

if len(ans_li) == 0:
    print(-1)
    exit()

print(min(ans_li))
