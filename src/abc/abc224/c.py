N = int(input())
li = []
count = 0

for i in range(N):
    xy = list(map(int, input().split()))
    li.append(xy)

for i in range(N):
    for k in range(i, N):
        for p in range(k, N):
            first = li[i]
            second = li[k]
            third = li[p]
            if not (first[1] - second[1]) * (first[0] - third[0]) == (first[1] - third[1]) * (first[0] - second[0]):
                count += 1

print(count)
