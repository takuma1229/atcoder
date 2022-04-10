import bisect

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans_li = []

B.append(10**100 * -1)
B.append(10**100)

A_s = sorted(A)
B_s = sorted(B)

for i in range(n):
    num = bisect.bisect_left(B_s, A_s[i])
    ans = min(abs(B_s[num-1] - A_s[i]), abs(B_s[num] - A_s[i]))
    ans_li.append(ans)

print(min(ans_li))
