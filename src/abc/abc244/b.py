N = int(input())
T = list(input())

direction_count = 0
x = 0
y = 0

for i in range(N):
    ti = T[i]
    if ti == "S":
        if direction_count % 4 == 0:
            x += 1
        elif direction_count % 4 == 1:
            y -= 1
        elif direction_count % 4 == 2:
            x -= 1
        elif direction_count % 4 == 3:
            y += 1
    else:
        direction_count += 1

print(f'{x} {y}')
