# -*- coding: utf-8 -*-
# 函数作为返回值
def lazy_sum(*args):
    def sum():
        nx = 0
        for n in args:
            nx += n
        return nx
    return sum

f1 = lazy_sum(1, 3, 5)
f2 = lazy_sum(2, 4, 6)
f3 = lazy_sum(1, 4, 5)
print(f1())
print(f2())
print(f3())