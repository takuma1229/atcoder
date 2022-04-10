X, Y = map(int, input().split())
A = [0] * 10 ** 6
A.append(0)

A[0] = X


for i in range(10 ** 6):
    A[i+1] = A[i] * 2
    if A[i+1] > Y:
        print(i+1)
        exit()
