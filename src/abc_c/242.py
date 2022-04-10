N = int(input())
count = 0

for i in range(N):
    if i == 0:
        count = 9
    else:
        count = (3*(count-(2**i))) + (2*(2**i))
    count = count % 998244353

print(count)
