n, m = map(int, input().split())
wa_num = [0] * n
ac_num = [0] * n
ac_count = 0
wa_count = 0

for i in range(m):
  p_str, s = map(str, input().split())
  p = int(p_str)
  if s == "AC" and ac_num[p-1] == 0:
    ac_count += 1
    ac_num[p-1] += 1 
  elif s == "WA" and ac_num[p-1] == 0:
    wa_count += 1
    wa_num[p-1] += 1

for i in range(n):
  if ac_num[i] == 0:
    wa_count -= wa_num[i]

print(str(ac_count) + " " + str(wa_count))

