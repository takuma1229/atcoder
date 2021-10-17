def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    split = len(nums) // 2
    left = nums[:split]
    right = nums[split:]

    left = merge_sort(left)
    right = merge_sort(right)

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums


n, k = map(int, input().split())
h_li = []

for i in range(n):
    h_li.append(int(input()))

h_s = merge_sort(h_li)

ans = 100000000000000000

for i in range(n-k+1):
    min_value = h_s[i]
    max_value = h_s[i+(k-1)]
    ans2 = max_value - min_value
    if ans2 < ans:
        ans = ans2

print(ans)
