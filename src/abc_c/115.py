n, k = map(int, input().split())
h_li = []

for i in range(n):
    h_li.append(int(input()))

# h_s = merge_sort(h_li)
h_s = sorted(h_li)

ans = 100000000000000000

for i in range(n-k+1):
    min_value = h_s[i]
    max_value = h_s[i+(k-1)]
    ans2 = max_value - min_value
    if ans2 < ans:
        ans = ans2

print(ans)
