def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


ans = 0

N = int(input())
a = list(map(int, input().split()))

for i in range(N):
    if not a[i] % 2 == 0:
        continue
    else:
        prime = prime_factorize(a[i])
        two_num = prime.count(2)
        ans += two_num

print(ans)
