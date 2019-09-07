# -*- coding: utf-8 -*-
"""
改行書式についての解説用例題コード

「普通に改行するだけだとエラーになる」の例
(動作しない)
"""


long_long_name_variable = "なが～いリテラル文字列"
more_variables = ("まだまだ伸びるよ～", "もういいんじゃね?")
finish_variable = "終わった..."

if long_long_name_variable == "なが～いリテラル文字列" and
    "まだまだ伸びるよ" not in more_variables and
    "さすがに長すぎぃ!!" != finish_variable:
    print("なげーよ")
