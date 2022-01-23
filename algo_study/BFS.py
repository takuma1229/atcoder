from collections import deque
import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]  # nは頂点の数、mは辺の数
g = [[] for _ in range(n)]  # 隣接リスト

# g[i]には頂点iと直接つながっている頂点番号を入れる
# 例えば、g[3] == [4,7]のとき、頂点3は頂点4,7と繋がっている。
# このようなリストを一般に「隣接リスト」という。（対になるのは「隣接行列」）
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    g[a].append(b)
    g[b].append(a)


def bfs(u):  # 頂点uからスタート
    queue = deque([u])
    d = [None] * n  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            # d[i]がNoneであるということは、すなわちiが検知済みでないということ。
            # 検知済みでない頂点には処理が必要。
            if d[i] is None:
                # iはvに隣接している（＝）ため、dist[i] = dist[v] + 1と言える。
                d[i] = d[v] + 1
                queue.append(i)
    return d


# 0からの各頂点の距離
d = bfs(0)
print(d)

# たどり着けない頂点はnoneが出る。
