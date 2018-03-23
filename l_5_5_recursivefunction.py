#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# fact
def fact(n):
   if n==1:
      return n
   return n*fact(n-1)

n=int(input("Please input your recursive function number: "))
print(fact(n))