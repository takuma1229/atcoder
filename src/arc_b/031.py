import copy

Map = []  # 10*10マスの地図
for _ in range(10):
    Map.append(list(input()))

# 4方向の移動ベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 現在地に隣接する陸地を海に置き換える


def dfs(x, y):
    # 今いるところをxに置き換える
    if New_map[x][y] == "o":
        New_map[x][y] = "x"
    for k in range(4):  # x方向にdx y方向にdy 移動した場所を(nx, ny)とする
        nx = x + dx[k]
        ny = y + dy[k]
        # nxとnyがMap内で陸地か判別
        if 0 <= nx < 10 and 0 <= ny < 10 and New_map[nx][ny] == "o":
            dfs(nx, ny)
    return


for i in range(10):
    for j in range(10):
        if Map[i][j] == "x":
            New_map = copy.deepcopy(Map)
            dfs(i, j)
        else:
          # その場所が陸なら特に何もしない
            continue

        flag = True

        # 全部たどり着けるなら、dfsの初期動作でNew_mapは全て"x"になっているはず。
        # なっていないならたどり着けていない場所があるということ。
        for a in range(10):
            for b in range(10):
                if New_map[a][b] == "o":
                    flag = False
        if flag:
            print("YES")
            exit()
else:
    print("NO")
