N = int(input())
A = list(map(int, input().split()))

A = sorted(A)

for i in range(2001):
    if not i in A:
        print(i)
        exit()
