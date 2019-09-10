# -*- coding: utf-8 -*-
"""
whileループについての解説用例題コード

前置判定だから最初からFalseだと処理されない例
"""

a = 3  # 最初からFalseになる条件
while a >= 5:
    print(a)
    a -= 1
print("ループ抜けたら{}でした".format(a))
