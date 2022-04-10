N, X = map(int, input().split())
S = list(input())

noseru = 10 ** 100
top = 2 ** (noseru)

for i in range(N):
    query = S[i]
    if query == "U":
        if X == 1:
            continue
        X = int(X//2)
    elif query == "L":
        X = X * 2
        if X > top:
            X = int(X//2)
    elif query == "R":
        X = (X*2)+1
        if X > top:
            X = int(X//2)
print(X)
