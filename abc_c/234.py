K = int(input())

ans_bin = bin(K)
ans_bin = list(str(ans_bin))

for i in range(len(ans_bin)):
    if ans_bin[i] == "1":
        ans_bin[i] = "2"

ans_bin = ans_bin[2:]
ans = "".join(ans_bin)
print(int(ans))
