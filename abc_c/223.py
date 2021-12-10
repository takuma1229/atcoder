N = int(input())
A_li = []
B_li = []
need_sec_li = []
passed_length = 0

for i in range(N):
    A, B = map(int, input().split())
    A_li.append(A)
    B_li.append(B)
    need_sec_li.append(A / B)

A_sum_li = [0] * N
A_sum_li[0] = A_li[0]


for i in range(1, N):
    A_sum_li[i] = A_li[i] + A_sum_li[i-1]

sec_middle = sum(need_sec_li) / 2
# print(sec_middle)

for k in range(N):
    if sec_middle - need_sec_li[k] > 0:
        sec_middle -= need_sec_li[k]
        passed_length += A_li[k]
    else:
        passed_length += B_li[k] * sec_middle
        print(passed_length)
        exit()

print(passed_length)
