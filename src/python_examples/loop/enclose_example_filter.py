# -*- coding: utf-8 -*-
"""
内包表記についての解説用例題コード

条件付きの例
"""

a = ['1', '23', '45', '67.8', '9.0']
print([float(i) for i in a if float(i) < 30.0])  # 数値として30未満の要素のみ対象
