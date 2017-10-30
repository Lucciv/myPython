#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#L5_1 函数
def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

x=int(input(please input your number: x= ))
n=int(input(please input your number: n= ))
print(power(x,n))