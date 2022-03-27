from audioop import reverse


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = reversed(A)
B = reversed(B)

X = [100000000] * N
