# import sys

N = int(input())

num_li = []

# リストを作っておく
for i in range((2*N)+1):
    num_li.append(i+1)

for i in range((2*N)+1):
    if i % 2 == 0:
        mine = num_li[0]
        print(mine)
        num_li.remove(mine)
        continue
    else:
        enemy = int(input())
        if enemy == 0:
            exit()
        num_li.remove(enemy)
        continue
