# -*- coding: utf-8 -*-
"""
whileループについての解説用例題コード

条件文でループが終わる例
"""

a = 10
while a >= 5:
    print(a)
    a -= 1
print("ループ抜けたら{}でした".format(a))
