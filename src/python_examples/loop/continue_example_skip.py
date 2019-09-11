# -*- coding: utf-8 -*-
"""
continue文についての解説用例題コード

探索処理で既定対象の時はスキップする例
"""

a = [1, 10, 3, 5, 29, 33, 120, 400, 7, 2, 12]
for elem in a:
    if elem > 10:  # 10より大きい値が見つかったら出力しないで続ける
        continue
    print(elem)
print("ループ最後の要素は{}でした".format(elem))
