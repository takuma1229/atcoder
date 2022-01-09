N = int(input())
S = input()
S = list(S)

count = 0


def delete_some_element(index, list):
    del list[index]


for i in range(len(S)):
    for k in range(len(S)):
        Si = delete_some_element(i, S)
        Sj = delete_some_element(k, S)
        print(Si)
        print(Sj)

# print(count)
