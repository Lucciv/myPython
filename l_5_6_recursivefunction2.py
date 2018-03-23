#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用递归函数移动汉诺塔:


def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)  # 把a上的n-1块移动到b
        move(1, a, b, c)  # 把a上的最后一块移动到c
        move(n - 1, b, a, c)  # 把b上的n-1块移动到c

move(2, 'A', 'B', 'C')