s_str = input()
s = list(s_str)
length = len(s)
ans_li = []
for i in range(length):
    s_last = s[-1]
    del s[-1]
    s.insert(0, s_last)
    ans = "".join(s)
    ans_li.append(ans)

ans_s = sorted(ans_li)
print(ans_s[0])
print(ans_s[-1])
