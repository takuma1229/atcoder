A, B, C, D = map(int, input().split())


def isPrime(num):  # 素数ならばその数を返す
    divisors = [1]
    if num == 1:
        return divisors
    for i in range(2, num//2+1):
        if num % i == 0:
            divisors.append(i)
    divisors.append(num)
    if len(divisors) == 2:
        return True


for i in range(A, B+1):
    ok_flag = True
    for k in range(C, D+1):
        if isPrime(i+k):
            ok_flag = False
    if ok_flag:
        print("Takahashi")
        exit()

print("Aoki")
