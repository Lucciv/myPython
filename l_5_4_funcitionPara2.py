#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# strtolist
# 把输入的字符串转换为列表
def strtolist(strnum):
    if strnum[1] == " " or strnum[-2] == " ":
        str = strnum.split(" ")
        listnum = [int(str[i]) for i in range(len(str))]
        return listnum
    else:
        str = strnum.split(",")
        listnum = [int(str[i]) for i in range(len(str))]
        return listnum

# product
# 计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积
def product(*number):
    s = 1
    for n in number:
        s = s * n
    return s

# Input String
strnum = input("Please input your list number(Split by \", or Space \"): ")
print(strtolist(strnum))

# Output Funcition
number = strtolist(strnum)
print(product(*number))