#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错,
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行

L1 = ['Hello', 'World', 0, 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)