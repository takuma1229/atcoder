import itertools

s, k_str = map(str, input().split())
k = int(k_str)
s_li = list(s)

ans_li = list(itertools.permutations(s_li))
ans_li_s = sorted(ans_li)
ans_li_s_u = list(set(ans_li_s))
ans_li_s_u_s = sorted(ans_li_s_u)
ans = ans_li_s_u_s[k-1]

print("".join(ans))
