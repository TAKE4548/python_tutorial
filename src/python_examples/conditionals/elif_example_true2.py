# -*- coding: utf-8 -*-
"""
elifによる条件分岐の例

ifの条件が偽ならifの中実行されなくて、elifの条件が真ならelifの中実行されて、
他は実行されないよっていう例
"""


a = 4
if a > 5:
    print("5より大きいです")
elif a > 2:
    print("2よりは大きいです")
elif a > 0:
    print("かろうじて正数です")
else:
    print("0以下です")
print("どっちでもいいよ…")
