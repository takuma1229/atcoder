abc = input()
a = int(abc[0])
b = int(abc[1])
c = int(abc[2])

abc = 100*a + 10*b + c
bca = 100*b + 10 * c + a
cab = 100 * c + 10 * a + b

print(abc + bca + cab)
