L, R = map(int, input().split())
S = input()
S = list(S)

former = []
former = S[:L-1]
# print(former)

latter = []
latter = S[R:]
# print(latter)

reversed_s = []
l_r = S[L-1:R]
# print(l_r)
reversed_s = list(reversed(l_r))
# print(reversed_s)

ans = former + reversed_s
# print(ans)
ans = ans + latter

print("".join(ans))
