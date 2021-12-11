N = int(input())
S = {}
for i in range(N):
    name = input()
    if name in S:
        S[name] += 1
    else:
        S[name] = 1

S_s = sorted(S.items(), key=lambda x: x[1])
print(S_s[-1][0])
