# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setup
   Description :
   Author :        Asdil
   date：          2018/8/2
-------------------------------------------------
   Change Activity:
                   2018/8/2:
-------------------------------------------------
"""
__author__ = 'Asdil'
from distutils.core import setup
from Cython.Build import cythonize

setup(name='test',
      ext_modules=cythonize("c_func.pyx"))