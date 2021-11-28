A, B = map(str, input().split())
max_length = max(len(A), len(B))
A = A.zfill(max_length)
B = B.zfill(max_length)
for i in range(max_length):
    if int(A[i]) + int(B[i]) > 9:
        print("Hard")
        exit()

print("Easy")
