# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     c_func
   Description :
   Author :        Asdil
   date：          2018/8/2
-------------------------------------------------
   Change Activity:
                   2018/8/2:
-------------------------------------------------
"""
__author__ = 'Asdil'

cpdef int fib_in_c(int n):
    cdef int i = 0
    for _ in range(n):
        for _ in range(n):
            i += 1
    return i

# def fib_in_c(n):
#     i = 0
#     for _ in range(n):
#         for _ in range(n):
#             i += 1
#     return i

# python setup.py build_ext --inplace