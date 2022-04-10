N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp1[i]...iまでを見たときにAiを選んでも問題ないかどうか
dp1 = [False] * N
dp2 = [False] * N

dp1[0] = True
dp2[0] = True

for i in range(1, N):
    if abs(A[i-1] - A[i]) <= K or abs(B[i-1] - A[i]) <= K:
        dp1[i] = True
    if abs(A[i-1] - B[i]) <= K or abs(B[i-1] - B[i]) <= K:
        dp2[i] = True

for i in range(N):
    if dp1[i] == False and dp2[i] == False:
        print("No")
        exit()

print("Yes")
