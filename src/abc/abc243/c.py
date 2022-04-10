N = int(input())

index_dict = {}

for i in range(N):
    X, Y = map(int, input().split())
    if Y in index_dict:
        index_dict[Y].append(i)
    else:
        index_dict[Y] = [i]

S = list(input())

dict_values = list(index_dict.values())
print(index_dict)
print(dict_values)
# print(S)

for value in dict_values:
    direction = []
    for idx in value:
        direction.append(S[idx])
    if len(set(direction)) == 2:
        print("Yes")
        exit()

print("No")
