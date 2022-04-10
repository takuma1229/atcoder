import math

l = int(input())

ans = int(math.factorial(l-1) / (math.factorial(11) * math.factorial(l-12)))

print(ans)

#200と199のときにWA