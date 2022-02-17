# import inspect
# import os


# def location(depth=0):
#     frame = inspect.currentframe().f_back
#     return os.path.basename(frame.f_code.co_filename), frame.f_code.co_name, frame.f_lineno


N, M = map(int, input().split())
matrix = []
[matrix.append(list(map(int, input().split()))) for i in range(N)]

past_row = matrix[0]  # 最初の行
past_value = matrix[0][0]  # 最初の値

for row_num in range(1, N):
    now_row = matrix[row_num]
    dif = now_row[0] % 7 - now_row[-1] % 7
    if not -5 <= dif <= 1:
        print("No")
        exit()

    if dif == 0:
        print("No")
        exit()
    for col_num in range(M):
        now_value = matrix[row_num][col_num]
        if now_value - past_value != 1:
            print("No")
            exit()
        else:
            past_value = now_value
        if now_row[row_num][col_num] - past_row[row_num][col_num] != 7:
            print("No")
            exit()
    past_row = now_row
