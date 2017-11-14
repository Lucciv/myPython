#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#L5_3_函数参数

# strtolist
# 把输入的字符串转换为列表
def strtolist(strnum):
   str=strnum.split(",")
   listnum=[int(str[i]) for i in range(len(str))]
   return listnum

# addpower
# x**1 + x**2 + x**3 + x**n的函数
def addpower(*number):
   s=0
   for n in number:
      s=s+n*n
   return s

strnum=input("Please input your list number(Split by \",\"): ")
print(strtolist(strnum))

number=strtolist(strnum)
print(addpower(*number))
