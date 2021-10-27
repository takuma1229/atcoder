A, B, C, X, Y = map(int, input().split())
ans = 0
xy_diff = max(X, Y) - min(X, Y)

# abピザが安くない場合。この場合、abピザを買う必要はなし
ans1 = (A * X + B * Y)

# ABピザを最小限買う場合
if X > Y:
    ans2 = C * (Y * 2) + A * xy_diff
elif Y > X:
    ans2 = C * (X * 2) + B * xy_diff
else:
    ans2 = C * Y * 2

# abピザを最大限買う場合
if X > Y:
    ans3 = C * (X * 2)
elif Y > X:
    ans3 = C * (Y * 2)
else:
    ans3 = C * (Y * 2)

print(min(ans1, ans2, ans3))
