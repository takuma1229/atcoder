li = [[1, 2], [1, 2]]


def unique_multi_dim_list(item):  # 多次元リストをユニーク化する
    list_u = list(map(list, set(map(tuple, item))))
    return(list_u)


print(unique_multi_dim_list(li))
