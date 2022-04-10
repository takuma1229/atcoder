S = input()
S = list(S)
K = int(input())
batu_li = []
dot_li = []
ans_li = []

for i in range(len(S)):
    if S[i] == ".":
        dot_li.append(i)
    else:
        batu_li.append(i)

for i in range(len(S)):
    if S[i] == ".":
        dot_num = dot_li.index(i)
        if dot_num + K < len(dot_li):
            ikeru_dot = dot_li[dot_num + K] - i + 1
            for k in range(i+1):
                if S[i-k] == "x":
                    ikeru_dot += 1
                else:
                    break
        else:
            ikeru_dot = dot_li[-1] - i + 1
            for k in range(i+1):
                if S[i-k] == "x":
                    ikeru_dot += 1
                else:
                    break
        ans_li.append(ikeru_dot)

if len(ans_li) == 0:
    print(len(S))
    exit()

print(max(ans_li))
