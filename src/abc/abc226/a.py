X = input()

if len(X) == 6:
    if int(X[3]) >= 5:
        print(int(float(X))+1)
    else:
        print(int(float(X)))
else:
    if int(X[2]) >= 5:
        print(int(float(X))+1)
    else:
        print(int(float(X)))
