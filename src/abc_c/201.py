import math


def permutations_count(n, r):  # nつからrつを選んで並べる順列の数
    return math.factorial(n) // math.factorial(n - r)


S = input()
S = list(S)
# 確実に含まれている数のリスト
include_li = []
# 含まれているかわからない数のリスト
prob_include_li = []

no_li = []

ans = 0

for i in range(10):
    if S[i] == "o":
        include_li.append(i)
    elif S[i] == "?":
        prob_include_li.append(i)
    elif S[i] == "x":
        no_li.append(i)


for i in range(10000):
    isOK = True
    num = str(i).zfill(4)
    num = list(num)
    for j in range(len(include_li)):
        if not str(include_li[j]) in num:
            isOK = False
    for k in range(len(no_li)):
        if str(no_li[k]) in num:
            isOK = False
    if isOK == True:
        ans += 1

print(ans)
