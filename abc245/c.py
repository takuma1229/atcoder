N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# A = reversed(A)
# B = reversed(B)
X = [100000000000] * N
for i in range(N-1):
    candidate = 20000000000
    one_li = [A[i], B[i]]
    two_li = [A[i+1], B[i+1]]
    for one_item in one_li:
        for two_item in two_li:
            if abs(one_item - two_item) <= K:
                if abs(one_item - two_item) <= candidate:
                    X[i] = one_item
                    candidate = abs(one_item - two_item)

An = A[N-1]
Bn = B[N-1]
if (abs(X[N-2] - An) <= K) or (abs(X[N-2] - Bn) <= K):
    X[N-1] = 1

if 100000000000 in X:
    print("No")
else:
    print("Yes")
