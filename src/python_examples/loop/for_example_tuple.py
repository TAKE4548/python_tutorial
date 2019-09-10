# -*- coding: utf-8 -*-
"""
forループについての解説用例題コード

tupleでも行けるよという例
"""

a = (1, 1.2, "34", [0, 9])  # tupleの例
print("こんなタプル\"{}\"から順次参照するよ～".format(a))
for elem in a:
    print(elem)
