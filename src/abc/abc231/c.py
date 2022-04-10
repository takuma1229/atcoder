import bisect
N, Q = map(int, input().split())
A = list(map(int, input().split()))
x = []
A_s = sorted(A)
# print(A)
for i in range(Q):
    x.append(int(input()))
    # from_right = bisect.bisect_left(A_s, x)
    # print("========")
    # print(from_right)
    # print(N)
    # print(N - from_right)

for i in range(len(x)):
    height = x[i]
    from_left = bisect.bisect_left(A_s, height)
    print(N - from_left)
