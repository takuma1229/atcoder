a = [1,2,3,4,5,6,7,8,9,10]

#累積和用リストの作成
s = [0] * 10

s[0] = a[0]

for i in range(1,10): #上の行でi=0の場合はもう実装済
  s[i] = s[i-1] + a[i]

print(s) # [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]