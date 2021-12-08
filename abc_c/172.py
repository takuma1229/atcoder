from itertools import accumulate
import bisect

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.insert(0, 0)  # Aを一冊も読まないパターンのために先頭に0を挿入
ans_li = [0]
A_cum = [0] * N
B_cum = [0] * M

A_cum[0] = A[0]
B_cum[0] = B[0]

for i in range(1, N):
    A_cum[i] = A_cum[i-1] + A[i]

for i in range(1, M):
    B_cum[i] = B_cum[i-1] + B[i]

# 全部読めちゃうパターン
if A_cum[-1] + B_cum[-1] <= K:
    print(N + M)
    exit()

# 一つも読めないパターン
if min(A[1], B[0]) > K:
    print(0)
    exit()


for i in range(N):
    # iはAを読む冊数
    A_time = A_cum[i]
    B_time = K - A_time
    # B_cumがどこまでB_timeを超えないか、二分探索する。
    # ここは最悪でもO(log200000) == 5.3010.....
    left = 0
    right = M-1
    B_num = bisect.bisect_left(B_cum, B_time)
    ans_li.append((i) + (B_num))

print(max(ans_li))
