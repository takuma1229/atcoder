N, X = map(int, input().split())

ball_num_li = []
ball_li = []
count = 0

for i in range(N):
    bag = list(map(int, input().split()))
    ball_num_li.append(bag[0])
    ball_li.append(bag[1:])


def dfs(x, y, product):
  # countがグローバル変数であることを宣言
    global count
    product = product * ball_li[y][x]

    if y == N-1:
        if product == X:
            count += 1
        # print(product)
        return

    for i in range(ball_num_li[y+1]):
        dfs(i, y+1, product)


for i in range(ball_num_li[0]):
    for k in range(ball_num_li[1]):
        dfs(k, 1, ball_li[0][i])

print(count)
