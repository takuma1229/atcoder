from functools import reduce
from math import gcd


def calculate_gcd(num_list: list) -> int:
    return reduce(gcd, num_list)


N, X = map(int, input().split())
x = list(map(int, input().split()))

distance = []

for x_item in x:
    distance.append(abs(X-x_item))


ans = calculate_gcd(distance)
print(ans)
