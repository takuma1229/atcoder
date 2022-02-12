S = input()

half = len(S) // 2

former_a_count = 0
latter_a_count = 0

former_flag = True
latter_flag = True

for i in range(len(S)):
    if latter_flag and S[len(S)-1-i] == "a":
        latter_a_count += 1
    else:
        latter_flag = False

    if former_flag and S[i] == "a":
        former_a_count += 1
    else:
        former_flag = False

    if former_flag == False and latter_flag == False:
        break

if latter_a_count - former_a_count < 0:
    print("No")
    exit()


additional = "a" * (latter_a_count - former_a_count)
# print(additional)
if len(additional) != 0:
    S = additional + S

# print(S)

print("Yes") if S == S[::-1] else print("No")
