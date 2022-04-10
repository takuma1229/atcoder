S = input()
S = list(S)
K = int(input())
count = 0

for i in range(100):
    if S[i] == "1":
        count += 1
    else:
        count += int(S[i]) ** (5000000 - 1)

    if count >= K:
        print(S[i])
        exit()

print(S[-1])
