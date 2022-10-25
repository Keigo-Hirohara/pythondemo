# -*- coding: utf-8 -*-
# 3-3  pandas のデータフレームを使ったプログラム例
import pandas as pd  #pandasをpdと置き換えることが多いです
indata = [('Tokyo', 175, 68, 25), ('Osaka', 183, 70, 23), ('Nagoya', 190, 72, 26)]
df = pd.DataFrame(data=indata, columns=['place', 'height', 'weight', 'Age'], \
                  index=['Hanako', 'Taro', 'Jiro' ]) #変数名dfはDataFrameの略
print("1----------\n",df)
print("2----------\n",df['weight'])
print("3----------\n",df[['weight', 'height']])
print("4----------\n",df['weight']['Hanako':'Taro'])
print("5----------\n",df['weight'][1:3])


print("6----------\n",df['weight'].sum())     # 合計。結果は210
print("7----------\n",df['weight'].mean())    # 算術平均。結果は70.0
print("8----------\n",df['weight'].median())  # 中央値。結果は70.0
print("9----------\n",df['weight'].max())     # 最大値。結果は72

import matplotlib.pyplot as plt #pandasでの可視化にpltの読み込みが必要
df['height'].plot.bar()  # pandasのデータフレームのメソッドplot.barを使う,各heightを棒グラフで表示
plt.show()

df.plot.scatter(x='weight', y='height') # heightとweightでの散布図
plt.show()


#df = pd.read_excel('read_test.xlsx', 'Sheet1')        # xlsxファイルのSheet1を読み込む場合
#df = pd.read_csv('read_test.csv', encoding='utf-8')  # CSVファイルを読み込む場合
#df.to_excel('output.xlsx', 'Sheet1')            # xlsxファイルを書き出す場合
#df.to_csv('output.csv')            # xlsxファイルを書き出す場合

df = pd.read_csv('sample.csv', encoding='utf-8') #sample.csvの読み込み
df['Timestamp']=pd.to_datetime(df['Timestamp'],unit='s') #時刻データへの変換
print("10----------\n",df.describe()) #基本統計量の計算

dict = {"year": [2012, 2016, 2020],
        "city": ["ロンドン", "リオデジャネイロ", "東京"]}
data = pd.DataFrame(dict)
print(data)

a = numpy.random.randint(1, 100, (3, 2)) #1から100の範囲でランダムに値を取り，3*2の行列を作成
frame = pd.DataFrame(a, columns=["a", "b"]) #各列にaとbのラベルを付ける
print(frame)
