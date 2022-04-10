S = input()
S = list(S)
first = S[0]
del S[0]
S.append(first)
print("".join(S))
