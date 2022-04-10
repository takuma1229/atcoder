import numpy as np
import string
alpha = list(string.ascii_lowercase)

N = int(input())
ans = []

while N > 0:
    decimal = N % 26
    N = N // 26
    chara = alpha[decimal-1]
    ans.append(chara)

print("".join(reversed(ans)))
