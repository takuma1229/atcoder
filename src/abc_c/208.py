N, K = map(int, input().split())
a = list(map(int, input().split()))
person_li = []

okashi_li = [0] * N


for i in range(1, N+1):
    person_num = a[i-1]
    person = (person_num, i)
    person_li.append(person)

person_li = sorted(person_li)

for i in range(10 ** 6):
    # if K >= N:
    #     okashi_li = list(map(lambda x: x+1, okashi_li))
    #     K -= N
    all_num = K // N
    okashi_li = list(map(lambda x: x+all_num, okashi_li))
    K = K % N
    for k in range(K):
        given_person = person_li[k][1]
        # print("givenperson")
        # print(given_person)
        okashi_li[given_person-1] += 1
    break


for i in range(N):
    print(okashi_li[i])
