#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Test

# 常量
MB = 1024
# 总容量
sddum = int(input("总容量(GB): "))
# GB转换MB
gb = sddum * MB
# 一天拿到的容量
nmb = int(input("每一天拿的容量数字(MB): "))
# 累计结果
time = gb / nmb
print("拿到总容量需要的天数：", time)
yed = time / 365
print("拿到总容量需要的年数：", yed)