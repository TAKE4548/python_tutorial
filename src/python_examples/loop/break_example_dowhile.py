# -*- coding: utf-8 -*-
"""
break文についての解説用例題コード

do ~ whileを再現する例
"""


a = 3  # 最初からFalseになる条件
while True:
    print(a)
    a -= 1
    if a < 5:  # aが5未満になったら抜ける
        break
print("ループ抜けたら{}でした".format(a))
