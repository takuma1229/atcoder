# いもす法

# import numpy as np

N, W = map(int, input().split())

water_use_amount_table = [0] * (2*(10**5) + 2)
water_left_table = [0] * (2*(10**5) + 2)
# water_use_amount_table = [0] * (100)
# water_left_table = [0] * (100)
# print(water_use_amount_table)

for i in range(N):
    S, T, P = map(int, input().split())
    water_use_amount_table[S] += P
    water_use_amount_table[T] -= P

for i in range(1, len(water_use_amount_table)):
    water_use_amount_table[i] += water_use_amount_table[i-1]

for i in range(len(water_use_amount_table)):
    water_left_table[i] += W
    water_left_table[i] -= water_use_amount_table[i]
    # print(f"left water : {water_left_table[i]}")
    if water_left_table[i] < 0:
        print("No")
        exit()

print("Yes")
# print(water_use_amount_table)
