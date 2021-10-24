N = int(input())

for i in range(1, 39):
    for k in range(1, 27):
        if (3 ** i) + (5 ** k) == N:
            print(str(i) + " " + str(k))
            exit()

print("-1")
