N = int(input())

ok_list = []

for i in range(2, (10**5) + 1):
    for k in range(2, 35):
        if i ** k <= N:
            ok_list.append(i ** k)
        else:
            break

ok_list = set(ok_list)
print(N - len(ok_list))
