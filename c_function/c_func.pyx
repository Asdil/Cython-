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
    if n < 2:
        return n
    return fib_in_c(n-2) + fib_in_c(n-1)