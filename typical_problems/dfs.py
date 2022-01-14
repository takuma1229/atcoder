# 再帰関数を使った実装
# sysを使っているため、python3で提出する！！！！！！！！！！！

import sys
sys.setrecursionlimit(10**7)  # 再帰関数の呼び出し制限
h, w = map(int, input().split())
c = [list(input()) for i in range(h)]


def dfs(x, y):
    # 壁に当たったり、探索範囲外になった場合はreturn
    if not(0 <= x < h) or not(0 <= y < w) or c[x][y] == "#":
        return
    if c[x][y] == "g":  # ゴールを見つけたら”Yes”を出力して終了
        print("Yes")
        sys.exit()

    c[x][y] = "#"  # 探索済みを示すためのマーキング
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)


# スタート位置を探索する。
for i in range(h):
    for j in range(w):
        if c[i][j] == "s":
            sx, sy = i, j  # スタート位置

dfs(sx, sy)
print("No")
