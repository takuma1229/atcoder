import itertools as iter

n = int(input())
town_li = []

for i in range(n):
  li = list(map(int, input().split()))
  town_li.append(li)

way_li = list(iter.permutations(town_li))
distance_sum_li = []

for i in range(len(way_li)):
  distance_sum = 0
  for k in range(1, n):
    distance = (((way_li[i][k][0] - way_li[i][k-1][0]) ** 2) + ((way_li[i][k][1] - way_li[i][k-1][1]) ** 2)) ** 0.5
    distance_sum += distance
  distance_sum_li.append(distance_sum)

average = sum(distance_sum_li) / len(way_li)
print(average)