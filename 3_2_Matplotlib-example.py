# -*- coding: utf-8 -*-
# 3-2  Matplotlib を使った単純なプロットのプログラム例
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)  # 0.0 ～ 0.5まで0.2刻みで配列に値を代入
plt.title('drawing example1')  # 図のタイトルの出力
# red dashes, blue squares and green triangles

plt.plot(t, t, 'r--', label='linear')    # y=xの直線。赤（r）でダッシュ（--）、名前はlinear
plt.plot(t, t**2, 'bs', label='square')  # y=x^2、青（b）で四角（s）、名前はsquare
plt.plot(t, t**3, 'g^', label='cube')    # y=x^3、緑（g）で三角（^）、名前はcube
plt.xlabel('x values')                   # x軸のタイトルはx values
plt.ylabel('y values')                   # y軸のタイトルはy values
plt.legend()                             # 凡例（はんれい，ぼんれいじゃないよ）を書く
plt.show()                               # この図を表示する
