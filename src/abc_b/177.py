S = input()
S = list(S)
T = input()
T = list(T)
ans_li = [0]


for i in range(len(S)-len(T)+1):
    count = 0
    flag = False
    if S[i] in T:
        flag = True
        for k in range(len(T)):
            if S[i+k] != T[k]:
                count += 1
    if flag and count == 0:
        print(0)
        exit()
    if flag:
        ans_li.append(count)


ans_li = list(set(ans_li))
ans_li = sorted(ans_li)
if len(ans_li) == 1:
    print(len(T))
    exit()
print(ans_li[1])
