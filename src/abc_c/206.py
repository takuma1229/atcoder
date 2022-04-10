N = int(input())
A = list(map(int, input().split()))
count = 0

A_s = sorted(A)
A_s_u = list(set(A_s))

if len(A_s_u) == 1:
    print(0)
    exit()

succession = 0

for i in range(1, N):
    if i == N-1:
        if succession != 0:
            if A_s[i] == A_s[i-1]:
                succession += 1
                count += (succession * (succession + 1)) / 2
                break
            else:
                count += (succession * (succession + 1)) / 2
                break
    if A_s[i] == A_s[i-1]:
        succession += 1
    else:
        if succession == 0:
            continue
        else:
            count += (succession * (succession + 1)) / 2
            succession = 0


print(int(((N * (N-1))/2)-count))
