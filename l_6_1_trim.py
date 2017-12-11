#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格

def trim(s):
    while s != '' and s[0] == ' ':
        s = s[1:]
    while s != '' and s[-1] == ' ':
        s = s[:-1]
    return s

s=input("Please input your string: ")
print(trim(s))