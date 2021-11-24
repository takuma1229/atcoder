import math

A, B, C, D = map(int, input().split())
C_candiv_num = (B // C) - ((A-1) // C)
D_candiv_num = (B // D) - ((A-1) // D)
# print(C_candiv_num)
# print(D_candiv_num)
lcm = int(C * D / (math.gcd(C, D)))
# print(lcm)
CD_candiv_num = int((B // lcm) - ((A-1) // lcm))

all_num = B - A + 1
ans = all_num - (C_candiv_num + D_candiv_num - CD_candiv_num)
if ans < 0:
    ans = 0

print(ans)
