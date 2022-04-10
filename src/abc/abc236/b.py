N = int(input())
A = list(map(int, input().split()))

all_sum = 0
for i in range(1, N+1):
    all_sum += 4 * i

my_sum = 0
for card in A:
    my_sum += card
print(all_sum - my_sum)
