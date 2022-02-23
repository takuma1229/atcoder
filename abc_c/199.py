import itertools

N = int(input())
S = input()
S = list(S)
Q = int(input())
# print(S)
left = S[:N]
right = S[N:]
L = [left, right]


for i in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        # S = list(S)
        S = list(itertools.chain.from_iterable(L))
        S[A-1], S[B-1] = S[B-1], S[A-1]
        left = S[:N]
        right = S[N:]
        L = [left, right]
        # S = "".join(S)
    else:
        left = S[:N]
        right = S[N:]
        L = [left, right]
        L[0], L[1] = L[1], L[0]
        # S = "".join(L)
    # print(S)

print("".join(list(itertools.chain.from_iterable(L))))
