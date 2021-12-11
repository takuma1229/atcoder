N, M = map(int, input().split())
person_count = [0] * N
query_list = []

# if M <= 1:
#     print("Yes")
#     exit()

# if N <= M:
#     print("No")
#     exit()

for i in range(M):
    sm_li = list(map(int, input().split()))
    # person_count[sm_li[0]-1] += 1
    # person_count[sm_li[1]-1] += 1
    query_list.append(sm_li)

query_list = list(map(list, set(map(tuple, query_list))))
print(query_list)
# def get_duplicate_list(seq):
#     seen = []
#     return [x for x in seq if not seen.append(x) and seen.count(x) == 2]


# duplicate_items = get_duplicate_list(query_list)
# print(duplicate_items)

# for i in range(len(duplicate_items)):
#     query_list.remove(duplicate_items[i])
# query_list.append(duplicate_items[i])

# print(query_list)

for i in range(len(query_list)):
    person_count[query_list[i][0]-1] += 1
    person_count[query_list[i][1]-1] += 1

one_count = 0
two_count = 0


for i in range(N):
    if person_count[i] > 2:
        print("No")
        exit()
    elif person_count[i] == 2:
        two_count += 1
    elif person_count[i] == 1:
        one_count += 1

if two_count <= N - 2:
    print("Yes")
else:
    print("No")
