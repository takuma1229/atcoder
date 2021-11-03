N = int(input())
dic = {}

for i in range(N):
    s = input()
    if s in dic.keys():
        dic[s] += 1
    else:
        dic[s] = 0

dic_s = sorted(dic.items(), key=lambda x: x[1], reverse=True)

if len(dic_s) == 1:
    print(dic_s[0][0])
    exit()


ans_li = []
ans_li.append(dic_s[0][0])

for i in range(1, N):
    if dic_s[i][1] == dic_s[i-1][1]:
        ans_li.append(dic_s[i][0])
    else:
        break


ans_li_s = sorted(ans_li)
for i in range(len(ans_li_s)):
    print(ans_li_s[i])
