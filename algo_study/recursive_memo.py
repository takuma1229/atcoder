# フィボナッチ数列をメモ化再帰で実装

memo = [0] * (50)  # 結果をメモ（グローバル変数で宣言！）


def fibnatch(n):
    if n <= 1:
        return 1
    else:
        if memo[n] == 0:
            memo[n] = fibnatch(n-1) + fibnatch(n-2)  # ここで再帰関数
        return memo[n]


print(fibnatch(4))  # 5
