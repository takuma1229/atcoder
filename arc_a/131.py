A = int(input())
B = int(input())

# print(str(B/2))

for i in range(10**8):
    aiu = list(str(B/2))
    del aiu[1]
    aiu = "".join(aiu)
    if str(A) in str(i) and str(aiu) in str(i):
        print(i)
        exit()
    else:
        continue
