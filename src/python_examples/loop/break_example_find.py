# -*- coding: utf-8 -*-
"""
break文についての解説用例題コード

探索処理で対象が見つかった時点で抜ける例
"""

a = [1, 10, 3, 5, 29, 33, 120, 400, 7, 2, 12]
for elem in a:
    if elem > 10:  # 10より大きい値が見つかったらその時点で抜ける
        break
    print(elem)
print("ループ最後の要素は{}でした".format(elem))
