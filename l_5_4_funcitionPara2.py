#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#L5_4_product

# strtolist
# 把输入的字符串转换为列表
def strtolist(strnum):
   str=strnum.split(",")
   listnum=[int(str[i]) for i in range(len(str))]
   return listnum

# product
# 计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积
def product(*number):
   s=1
   for n in number:
      s=s*n
   return s

strnum=input("Please input your list number(Split by \",\"): ")
print(strtolist(strnum))

number=strtolist(strnum)
print(product(*number))