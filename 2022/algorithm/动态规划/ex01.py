#! /user/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 23/2/21
@version: 0.1
@description: 递归实现斐波那且数列
"""
def f(N):
    if N == 1 or N == 2:
        return 1
    return f(N - 1) + f(N - 2)
    
