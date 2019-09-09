# -*- coding: utf-8 -*-
"""
elifによる条件分岐の例

ifもelifもすべて条件が偽ならelseの中実行されて、他は実行されないよっていう例
"""


a = -1
if a > 5:
    print("5より大きいです")
elif a > 2:
    print("2よりは大きいです")
elif a > 0:
    print("かろうじて正数です")
else:
    print("0以下です")
print("どっちでもいいよ…")
