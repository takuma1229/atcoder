data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
K = 20

left = 0
right = len(data) - 1
while left <= right:
    mid = (left + right) // 2
    if data[mid] == K:
        print(mid)
        exit()
    elif data[mid] < K:
        left = mid + 1
    elif data[mid] > K:
        right = mid - 1

print("not found")
