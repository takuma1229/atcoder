s = input()
s = list(s)
num = len(s) - 2
ans_li = []
ans_li.append(s[0])
ans_li.append(str(num))
ans_li.append(s[-1])
print("".join(ans_li))
