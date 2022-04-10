S = input()
S = list(S)
alp = "abcdefghijklmnopqrstuvwxyz"
alp = list(alp)

for i in range(len(S)):
    if S[i] in alp:
        alp.remove(S[i])

if len(alp) > 0:
    print(alp[0])
else:
    print("None")
