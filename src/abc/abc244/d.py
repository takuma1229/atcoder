S = list(map(str, input().split()))
T = list(map(str, input().split()))

if S == T:
    print("Yes")
elif S[0] == T[2] and S[1] == T[0]:
    print("Yes")
elif S[0] == T[1] and S[1] == T[2]:
    print("Yes")
else:
    print("No")
