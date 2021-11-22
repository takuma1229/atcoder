N, X = map(int, input().split())
A = list(map(int, input().split()))
friend_li = [0] * N
next_friend = X


for i in range(N):
    first_friend = next_friend
    friend_li[first_friend - 1] += 1
    next_friend = A[first_friend-1]

print(N - friend_li.count(0))
