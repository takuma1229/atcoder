N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_set = set(A)
B_set = set(B)

one_count = 0
two_count = 0

for i in range(N):
    if A[i] == B[i]:
        one_count += 1

print(one_count)

two = A_set & B_set
print(len(two)-one_count)
