#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#L5_1 函数
x=6
n=3
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(x,n))