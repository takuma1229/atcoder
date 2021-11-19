s = input()
ans_li = []

for i in range(len(s)):
    if i % 2 == 0:
        ans_li.append(s[i])

print("".join(ans_li))
