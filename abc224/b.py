h, w = map(int, input().split())
li = []

for i in range(h):
    A = list(map(int, input().split()))
    li.append(A)

for i in range(h):
    for k in range(i):
        for p in range(w):
            for t in range(p):
                if not li[i][p] + li[k][t] <= li[k][p] + li[i][t]:
                    print("No")
                    exit()

print("Yes")
