N = int(input())
s_li = [input() for i in range(N)]

s_li_new = []
anagram_dict = {}

ans = 0

for index, string in enumerate(s_li):
    sorted_string = sorted(string)
    s_li[index] = sorted_string

for index, string in enumerate(s_li):
    sorted_string = "".join(string)
    s_li[index] = sorted_string

for i, string in enumerate(s_li):
    # string = s_li[i]
    if string in anagram_dict:
        anagram_dict[string] += 1
    else:
        anagram_dict[string] = 1

for c in list(anagram_dict.values()):
    if c != 1:
        ans += (c*(c-1)) / 2

print(int(ans))
