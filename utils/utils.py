import math
from math import gcd
from functools import reduce
import numpy as np


def prime_factorize(n):  # 素因数分解してリストで返す
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


def divisors_list_h(num):  # 約数をリストとして返す
    divisors = [1]
    if num == 1:
        return divisors
    for i in range(2, num//2+1):
        if num % i == 0:
            divisors.append(i)
    divisors.append(num)
    return divisors


def manhattan_distance(point_a, point_b):  # xy座標における二点間のマンハッタン距離を求める
    a = np.array(point_a)
    b = np.array(point_b)
    return(np.linalg.norm(a-b, ord=1))


def permutations_count(n, r):  # nつからrつを選んで並べる順列の数
    return math.factorial(n) // math.factorial(n - r)


def unique_multi_dim_list(list):
    return list(map(list, set(map(tuple, list))))


def calculate_gcd(num_list: list) -> int:
    return reduce(gcd, num_list)
