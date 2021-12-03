N, K = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = N-1

while left <= right:
    mid = (left + right) // 2
    if A[mid] >= K:
        if A[mid-1] < K:
            print(mid)
            exit()
        else:
            right = mid - 1
    else:
        left = mid + 1


print(-1)
