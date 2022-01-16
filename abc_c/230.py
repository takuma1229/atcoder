N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

ans_li = []

for i in range(P, Q+1):
    sm_li = []
    for j in range(R, S+1):
        if i-j == A-B or i+j == A+B:
            sm_li.append("#")
        else:
            sm_li.append(".")
    ans_li.append(sm_li)

for i in range(len(ans_li)):
    print("".join(ans_li[i]))
