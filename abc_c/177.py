n = int(input())
A = list(map(int, input().split()))

print(((sum(A) * 2) - 1) % ((10 ** 9) + 7))