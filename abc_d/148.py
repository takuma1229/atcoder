import copy

N = int(input())
a = list(map(int, input().split()))

if not 1 in a:
    print(-1)
    exit()


now_count = -1
last_count = 0
now_index = -1

for i in range(1, N):
    if i in a:
        now_index = a.index(i)
        # a = copy.deepcopy(a[now_index+1:])
        del a[:now_index+1]
        # print(f"now: {now_index}, i:{i}")
        # print(f"a: {a}")
        last_count = i
    else:
        last_count = i-1
        break

# print(f"last count {last_count}")
# print(f"now count {now_count}")

if last_count == N or last_count == 0:
    print(0)
else:
    print(N-last_count)
