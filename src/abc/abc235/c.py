N, Q = map(int, input().split())
a = list(map(int, input().split()))
li = []
dict = {}

for i in range(N):
    num = a[i]
    num = str(num)
    if not num in dict.keys():
        dict[num] = []
        dict[num].append(i+1)
    else:
        dict[num].append(i+1)

for i in range(Q):
    x, k = map(int, input().split())
    if not str(x) in dict.keys():
        print(-1)
    else:
        indexes = dict[str(x)]
        length = len(indexes)
        # print(indexes)
        if length >= k:
            print(indexes[k-1])
        else:
            print(-1)
