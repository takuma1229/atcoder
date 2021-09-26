#みかん（100円）りんご（200円）ぶどう（300円）がそれぞれ1つずつ果物屋さんにありました。
#財布の中には300円ありますが、考え得るすべての買い物パターンを列挙しなさい。

money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)

for i in range(2 ** n): #bit全探索は2**n通りについて調べる
  bag = []
  total = 0
  for j in range(n): #j番目の荷物を買うかをbitで判定
    if ((i >> j) & 1): #iをj回右シフトして、jが1であるかどうかを判定。
      bag.append(item[j][0]) #jが1であるならば、bagにj番目のitemを入れる
      total += item[j][1] #金額にも加算。
    if (total <= money):
      print(total, bag) #bagに入っている総額が300以下なら、買ったものと総額をprint