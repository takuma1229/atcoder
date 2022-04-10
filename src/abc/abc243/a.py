V, A, B, C = map(int, input().split())
V = V % (A+B+C)
V = V - A
if V < 0:
    print("F")
    exit()
V = V-B
if V < 0:
    print("M")
    exit()
V = V-C
if V < 0:
    print("T")
    exit()
