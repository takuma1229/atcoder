import itertools

N = int(input())
S = input()
S = list(S)
Q = int(input())
flip = False

for i in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if not flip:
            S[A-1], S[B-1] = S[B-1], S[A-1]
        else:
            S[len(S)-(A-1)-1], S[len(S)-(B-1) -
                                 1] = S[len(S)-(B-1)-1], S[len(S)-(A-1)-1]
    else:
        if flip:
            flip = False
        else:
            flip = True


if flip:
    S[:N], S[N:] = S[N:], S[:N]
    print("".join(S))
else:
    print("".join(S))
