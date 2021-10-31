N = int(input())


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


li = [0] * (N-1)


def divisors_list_h(num):
    divisors = [1]
    if num == 1:
        return divisors
    for i in range(2, num//2+1):
        if num % i == 0:
            divisors.append(i)
    divisors.append(num)
    return divisors


for i in range(1, N):
    devisor_num = len(divisors_list_h(i))
    li[i-1] = devisor_num

print(sum(li))
