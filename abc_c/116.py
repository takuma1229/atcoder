N = int(input())
h = list(map(int, input().split()))  # hは目標となる花の高さ

time = 0

for i in range(100):
    last_watered = 0
    if h.count(0) == N:
        print(time)
        exit()
    # print(h)
    for i in range(N):
        if i != N-1:
            if h[i] == 0:
                if last_watered == i:
                    continue
                else:
                    interval = i - last_watered
                    zero_time = 0
                    for k in range(last_watered, i):
                        h[k] -= 1
                        if h[k] < 0:
                            h[k] = 0
                            zero_time += 1
                    last_watered = i
                    if not zero_time == interval:
                        time += 1
        else:
            if h[i] == 0:
                if last_watered == i:
                    continue
                else:
                    interval = i - last_watered
                    zero_time = 0
                    for k in range(last_watered, i):
                        h[k] -= 1
                        if h[k] < 0:
                            h[k] = 0
                            zero_time += 1
                    last_watered = i
                    if not zero_time == interval:
                        time += 1
            else:
                for k in range(last_watered, N):
                    h[k] -= 1
                    if h[k] < 0:
                        h[k] = 0
                time += 1

print(time)
