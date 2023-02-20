#! /user/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 23/2/20
@version: 0.1
@description: 使用递归找最小值
"""

def Min(a, i):
    if i == 0:
        return a[0]
    else:
        min = Min(a, i-1)
        if min > a[i]:
            return a[i]
        else:
            return min
        
a = [3, 2, 1, 5, 4, 0]
print(Min(a, 5))