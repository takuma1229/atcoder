S1 = input()
S2 = input()
if S1 == ".#":
    if S2 == "#.":
        print("No")
        exit()
elif S1 == "#.":
    if S2 == ".#":
        print("No")
        exit()

print("Yes")
