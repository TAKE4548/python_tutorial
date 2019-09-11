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

c = {
    (0, 0): 'a', (0, 1): 'b', (0, 2): 'c',
    (1, 0): 'd', (1, 1): 'e', (1, 2): 'f',
    (2, 0): 'g', (2, 1): 'h', (2, 2): 'i'
}
print("左上2x3で取得")
print([c[(i, j)] for i in range(3) for j in range(2)])
print()
print("右下2x2で取得")
print([c[(i, j)] for i in range(1, 3) for j in range(1, 3)])
print()

d = [[0, 1], [2, 3], [4, 5]]
print("2次元配列を1次元配列に")
print([j for i in d for j in i])
