#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple

# strtolist
# 把输入的字符串转换为列表
def strtolist(s):
    d = s.split(',')
    l = [int(d[i]) for i in range(len(d))]
    return l

# findMinAndMax
# 查找一个list中最小和最大值
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

s = input("Please input your string: ")
L = strtolist(s)
print(findMinAndMax(L))
