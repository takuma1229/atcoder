n = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
ans_li = []

for i in range(n):
    A1_sum = sum(A1[:i+1])
    A2_sum = sum(A2[i:])
    ans_li.append(A1_sum + A2_sum)

print(max(ans_li))
