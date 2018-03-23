#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# L5_2_二元一次方程
import math

def myquadratic(a, b, c):
    ader = b**2 - 4 * a * c
    if ader > 0:
        x1 = (-b + math.sqrt(ader)) / (2 * a)
        x2 = (-b - math.sqrt(ader)) / (2 * a)
        return x1, x2
    elif ader == 0:
        x1 = x2 = -b / 2 * a
        return x1, x2
    elif a == 0:
        x = -c / b
        return x
    else:
        return('此方程无解')

# 测试
if myquadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif myquadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')