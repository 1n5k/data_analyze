import matplotlib.pyplot as plt
x = [0,1,2,3,4]
y = [10,20,15,30,50]

## X軸、Y軸のスケールをきめる(下の場合はX 0～5, Y 0～60)
plt.axis([0,5,0,60])

## ラベルを定義
n = ["A","B","C","D","E"]

## X軸とY軸を定義
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

## ラベルと軸の対応
for i in lange(len(n)):
    plt.annotate(n[i], xy=(x[i]+0.1, y[i]+2.0))

plt.plot(x,y)
plt.show()

## 線のの太さや色、スタイルも設定できる。
# plt.plot(x,y, linewidth = 3, color = 'red')
# plt.plot(x,y, linestyle = 'dashed')

## 散布図にするにはplt.scatter(x,y)を使う。
# plt.scatter(x,y)

## ピアソン相関係数で相関をとる
