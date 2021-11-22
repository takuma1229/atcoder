N, K = map(int, input().split())
point_li = []
for i in range(N):
    points = list(map(int, input().split()))
    point_sum = sum(points)
    point_li.append(point_sum)

point_sorted = sorted(point_li, reverse=True)

k_student = point_sorted[K-1]

for i in range(N):
    i_student = point_li[i]
    if i_student + 300 >= k_student:
        print("Yes")
    else:
        print("No")
