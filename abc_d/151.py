H, W = map(int, input().split())

li = []
ans_li = []

for i in range(H):
    sm_li = list(input())
    li.append(sm_li)


def dfs(sx, sy, gx, gy):
    stack = [[sx, sy]]
    visited = [[0 for i in range(W)]for j in range(H)]
    visited[sx][sy] = 1

    dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    move_count = 0

    while stack:
        x, y = stack.pop()  # 要素を取り出す
        for i in range(4):
            nx, ny = x+dx_dy[i][0], y+dx_dy[i][1]  # 現在の位置
            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny] == 0 and li[nx][ny] != '#':
                visited[nx][ny] = 1  # 訪れた印をつける
                stack.append([nx, ny])  # スタックに現在位置をpush
                move_count += 1
        if visited[gx][gy] == 1:
            return(move_count)


for h1 in range(H):
    for h2 in range(H):
        for w1 in range(W):
            for w2 in range(W):
                if h1 == h2 and w1 == w2:
                    ans_li.append(0)
                    continue
                else:
                    if li[h1][w1] == ".":
                        li[h1][w1] = "s"
                        sx, sy = h1, w1
                    else:
                        continue
                    if li[h2][w2] == ".":
                        li[h2][w2] = "g"
                        gx, gy = h2, w2
                    else:
                        continue
                    move = dfs(sx, sy, gx, gy)
                    ans_li.append(move)

print(max(ans_li))
