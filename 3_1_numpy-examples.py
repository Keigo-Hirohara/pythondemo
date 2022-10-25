# -*- coding: utf-8 -*-
# 3-1  数値計算ライブラリ NumPy

import numpy as np  #numpyをnpと置き換えることが多いです

na = np.array( [[1, 3, 5], [2, 4, 6]] )    # 2次元listをNumPyの配列に変換してnaに代入
nb = np.array( [[1, 4, 7], [10, 13, 16]] )
print("1----------\n",na + nb)             # 配列naとnbの和
print("2----------\n",na * nb)             # 配列naとnbの要素ごとの積
print("3----------\n",na.dot(nb.T))        # 配列naに配列nb.Tを掛ける（行列の積），.Tは転置のこと
#print(np.dot(na, nb.T))   # 同上
print("4----------\n",na[1, 2])
print("5----------\n",na.shape) # naの各次元のサイズ確認．この場合(2,3)のタプルで，2×3の行列
print("6----------\n",na.reshape(3,2)) # naを3×2の行列に変換する．代入していないのでこの時だけ．
print("7----------\n",na.T) # naの転置行列．こちらも代入していないのでna自体はそのまま．

# 逆行列
a = np.array([[1., 3.], [2., 4.]])
print("8----------\n",np.linalg.inv(a))
#   array([[-2. ,  1.5],
#          [ 1. , -0.5]]) → これは出力結果の説明
#-2. や1. はそれぞれ-2.0, 1.0の意味

# 固有値，固有ベクトル計算
matrix = np.array([[3,1],[2,4]])
w,v=np.linalg.eig(matrix)
print("9----------\n",w) # 固有値
print("10----------\n",v) # 固有ベクトル　演算結果は実行して確認してください．
