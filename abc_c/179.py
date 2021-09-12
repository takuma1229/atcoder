n = int(input())
count = 0
#n - c = a * b
#cはn-1通り存在する
#a or b == 1 となるような組み合わせは2*(n-1)通り
#a or b == 1 ではないような組み合わせはn-cの1とn-c以外の約数の個数*2通り

def isPrime(n):
  if n < 2:
    # 2未満は素数でない
    return False
  if n == 2:
    # 2は素数
    return True
  for p in range(2, n):
      if n % p == 0:
        # nまでの数で割り切れたら素数ではない
        return False
  # nまでの数で割り切れなかったら素数
  return True

for a in range(n):
  if not isPrime(a):
    count += 1

print(2*(n-1) + count*2)