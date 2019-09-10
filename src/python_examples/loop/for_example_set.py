# -*- coding: utf-8 -*-
"""
forループについての解説用例題コード

setでも行けるよという例
"""

a = {10, 1.2, "34", 1.2, 3, }  # setの例
print("こんな集合\"{}\"から順次参照するよ～".format(a))
for elem in a:
    print(elem)
