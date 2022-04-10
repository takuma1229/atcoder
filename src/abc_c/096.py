H, W = map(int, input().split())
s = []

for i in range(H):
    s_li = input()
    s.append(s_li)

for h in range(H):
    for w in range(W):
        now_search = s[h][w]
        if now_search == ".":
            continue
        # 例外を順に処理していく。まずは四隅から。次に四隅を抜いた各辺について。
        if h == 0 and w == 0:  # 左上
            if s[h+1][w] == "." and s[h][w+1] == ".":
                print("No")
                # print(str(h) + str(w))
                exit()
        elif h == 0 and w == W-1:  # 右上
            if s[h+1][w] == "." and s[h][w-1] == ".":
                print("No")
                # print(str(h) + str(w))
                exit()
        elif h == H-1 and w == 0:  # 左下
            if s[h-1][w] == "." and s[h][w+1] == ".":
                print("No")
                # print(str(h) + str(w))
                exit()
        elif h == H-1 and w == W-1:  # 右下
            if s[h-1][w] == "." and s[h][w-1] == ".":
                print("No")
                # print(str(h) + str(w))
                exit()
        elif h == 0:  # 上の辺
            if s[h][w+1] == "." and s[h][w-1] == "." and s[h+1][w] == ".":
                print("No")
                # print(str(h) + str(w))
                exit()
        elif h == H-1:  # 下の辺
            if s[h][w+1] == "." and s[h][w-1] == "." and s[h-1][w] == ".":
                print("No")
                # print(str(h) + str(w))
                exit()
        elif w == 0:  # 左の辺
            if s[h][w+1] == "." and s[h-1][w] == "." and s[h+1][w] == ".":
                print("No")
                # print(str(h) + str(w))
                exit()
        elif w == W-1:  # 右の辺
            if s[h][w-1] == "." and s[h-1][w] == "." and s[h+1][w] == ".":
                print("No")
                # print(str(h) + str(w))
                exit()
        else:  # 最後に普通のマス
            if s[h][w-1] == "." and s[h-1][w] == "." and s[h+1][w] == "." and s[h][w+1] == ".":
                print("No")
                # print(str(h) + str(w))
                exit()

print("Yes")
