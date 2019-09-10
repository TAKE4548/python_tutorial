# -*- coding: utf-8 -*-
"""
forループについての解説用例題コード

多次元配列に便利な例
"""

a = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]  # タプルのリスト
print("タプルのままで受けます")
for elem in a:
    print(elem)

print("最初から分けて受けます")
for elem1, elem2, elem3 in a:
    print(elem1, elem2, elem3)

print("要素数があってないとダメです")
for elem1, elem2 in a:
    print(elem1, elem2)