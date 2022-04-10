# print(int(abs(-2.4)))
import math
from fractions import Fraction
X = input()
if X == "0":
    print(X)
    exit()
X = int(X)
if -10 < X < 0:
    print(-1)
    exit()
elif 0 < X < 10:
    print(0)
    exit()
if X < 0:
    strX = str(X)
    last = strX[-1]
    if last == "0":
        print(strX[:len(strX)-1])
    else:
        ans_abs = strX[1:len(strX)-1]
        print((int(ans_abs) + 1) * (-1))
else:
    strX = str(X)
    print(strX[:len(str(X))-1])
