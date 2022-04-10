A = list(map(int, input().split()))
A = sorted(A, reverse=True)
ok = True
dif = A[1] - A[0]
for i in range(1, len(A)):
    if not A[i] - A[i-1] == dif:
        ok = False

if ok:
    print("Yes")
else:
    print("No")
