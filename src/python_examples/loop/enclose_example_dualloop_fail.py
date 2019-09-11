# -*- coding: utf-8 -*-
"""
内包表記についての解説用例題コード

多重ループの例
"""

a = [[0, 1], [2, 3], [4, 5]]
print("2次元配列を1次元配列に")
print([i for i in j for j in a])
