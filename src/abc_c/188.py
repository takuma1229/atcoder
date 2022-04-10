N = int(input())
A = list(map(int, input().split()))

half = (2 ** N // 2)

former_max = max(A[:half])
latter_max = max(A[half:])

second = min(former_max, latter_max)
print(A.index(second) + 1)
