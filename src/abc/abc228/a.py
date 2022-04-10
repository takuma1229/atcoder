S, T, X = map(int, input().split())

if S < T:
    if T == 0:
        T += 24

    if S <= X < T:
        print("Yes")
    else:
        print("No")
else:
    if S == 0:
        S += 24
    if T <= X < S:
        print("No")
    else:
        print("Yes")
