N = int(input())
h = list(map(int, input().split()))

now_flog = 0
cost = 0

for i in range(N):
    if now_flog == N-2:
        cost += abs(h[N-1] - h[N-2])
        print(cost)
        exit()
    elif now_flog == N-1:
        print(cost)
        exit()

    now_height = h[now_flog]
    one_height = h[now_flog + 1]
    two_height = h[now_flog + 2]
    now_to_one = abs(now_height - one_height)
    now_to_two = abs(now_height - two_height)
    one_to_two = abs(one_height - two_height)
    # print("===================")
    # print(now_to_one)
    # print(now_to_two)
    # print(one_to_two)
    # print("===================")

    if now_to_two < now_to_one + one_to_two:
        cost += now_to_two
        now_flog += 2
        # print("飛ばして飛んだよ")
        # print(now_flog)
        # print(one_to_two)
        continue
    else:
        cost += now_to_one
        now_flog += 1
        # print("飛ばしてないよ")
        # print(now_flog)
        # print(now_to_one)
        continue
