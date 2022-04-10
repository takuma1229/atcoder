N = int(input())
A = list(map(int, input().split()))
count = 0

li = [0] * 200

for i in range(N):
    decimal = A[i] % 200
    li[decimal] += 1

for i in range(200):
    num = li[i]
    count += num * (num-1) / 2

print(int(count))
