#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def findMinAndMax(L):
    # 检查数据类型
    if not isinstance(L, list):
        print('数据类型错误')
        return L
    # 检查是否为空列表
    elif len(L) == 0:
        return(None, None)
    # 若list里只有一个元素，返回初始定义的最大最小数值
    elif len(L) == 1:
        return(L[0], L[0])
    # 多于一个元素，遍历列表查找最小，最大值
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if min > i:
                min = i
            if max < i:
                max = i
        return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
