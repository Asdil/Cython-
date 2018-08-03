# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     map
   Description :
   Author :        Asdil
   date：          2018/8/3
-------------------------------------------------
   Change Activity:
                   2018/8/3:
-------------------------------------------------
"""
__author__ = 'Asdil'
import time
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool  # 多线程池
from multiprocessing import Pool  # 多进程池
import time


def add(x, y):
    i = 0
    for i in range(x):
        for j in range(y):
            i+=1
    return i


def add_wrap(args):
    return add(*args)


if __name__ == "__main__":
    # 多线程池
    # thread_pool = ThreadPool(4) # 池的大小为4
    # star = time.time()
    # print(thread_pool.map(add_wrap, [(1000,2000),(3000,4000),(5000,6000)]))
    # thread_pool.close()
    # thread_pool.join()
    # end = time.time()
    # print('多线程用时', end-star)

    # 多进程池
    pool = Pool(4)
    star = time.time()
    print(pool.map(add_wrap, [(1000,2000),(3000,4000),(5000,6000)]))
    pool.close()
    pool.join()
    end = time.time()
    print('多线程用时', end - star)

    #close the pool and wait for the worker to exit



    # 多线程不用close join用时 2.8903489112854004
    # 多线程用时 3.013291597366333


    # 多线程不用colse join用时 2.211496114730835
    # 多线程用时 2.0693838596343994

