# -*- coding: utf-8 -*-
"""
内包表記についての解説用例題コード

多重ループの例
"""

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 0]
print("総組合せ参照")
print([i * j for i in a for j in b])
print()
print("i<3フィルタ付き")
print([i * j for i in a for j in b if i < 3])
