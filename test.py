# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :        Asdil
   date：          2018/8/2
-------------------------------------------------
   Change Activity:
                   2018/8/2:
-------------------------------------------------
"""
__author__ = 'Asdil'
from c_function import c_func
import time
from numba import jit
@jit(nopython=True)
def fib_in_c(n):
    i = 0
    for _ in range(n):
        for _ in range(n):
            i += 1
    return i

star = time.time()
c = fib_in_c(10000)
end = time.time()

print(end - star, c)

# 3.6077160835266113 100000000
# 4.76837158203125e-06 100000000
# 6.598441123962402 100000000
# 0.21131277084350586 100000000

