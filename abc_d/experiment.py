import copy

li = [1, 2, 3]
li_c = copy.deepcopy(li)

print(li_c)

li_c[0] = 100000

print(li)
print(li_c)
