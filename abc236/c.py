N, M = map(int, input().split())
S = list(map(str, input().split()))
T = list(map(str, input().split()))

station_dict = {}

for station in S:
    station_dict[station] = False

S_set = set(S)
T_set = set(T)

S_T_set = S_set & T_set

for station in S_T_set:
    station_dict[station] = True

keys = station_dict.keys()

for name in keys:
    if station_dict[name]:
        print("Yes")
    else:
        print("No")
