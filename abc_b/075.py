H, W = map(int, input().split())
S = []
ans_li = []
for i in range(H):
    li = input()
    li = list(li)
    S.append(li)

for i in range(H):
    sm_li = []
    for k in range(W):
        num = 0
        if S[i][k] == "#":
            sm_li.append("#")
        else:
            # まず四隅から実装
            if i == 0 and k == 0:  # 左上
                num = S[i][k:k+2].count(".") + S[i+1][k:k+2].count(".") - 1
            elif i == 0 and k == W-1:  # 右上
                num = S[i][k-1:k+1].count(".") + S[i+1][k-1:k+1].count(".") - 1
            elif i == H-1 and k == 0:  # 左下
                num = S[i-1][k:k+2].count(".") + S[i][k:k+2].count(".") - 1
            elif i == H-1 and k == W-1:
                num = S[i-1][k-1:k+1].count(".") + S[i][k-1:k+1].count(".") - 1
            # 次に各例外行列を実装していく
            elif i == 0:  # 上の行
                num = S[i][k-1:k+2].count(".") + S[i+1][k-1:k+2].count(".") - 1
            elif i == H-1:  # 下の行
                num = S[i][k-1:k+2].count(".") + S[i-1][k-1:k+2].count(".") - 1
            elif k == 0:  # 左の列
                num = S[i-1][k:k+2].count(".") + S[i][k:k +
                                                      2].count(".") + S[i+1][k:k+2].count(".") - 1
            elif k == W-1:  # 右の列
                num = S[i-1][k-1:k+1].count(".") + S[i][k-1:k +
                                                        1].count(".") + S[i+1][k-1:k+1].count(".") - 1
            else:  # 最後に普通のパターン
                num = S[i-1][k-1:k+2].count(".") + S[i][k-1:k +
                                                        2].count(".") + S[i+1][k-1:k+2].count(".") - 1
        sm_li.append(str(num))
    ans_li.append(sm_li)

for i in range(H):
    print("".join(ans_li[i]))
