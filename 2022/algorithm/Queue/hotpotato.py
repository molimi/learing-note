#! /user/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: CarpeDiem
@date: 22/12/8
@version: 0.1
@description: 热土豆问题
"""
import queue

def hot_potato(namelist, nums):
    sim_queue = queue.Queue()
    for name in namelist:
        sim_queue.enqueue(name)
    
    while sim_queue.size() > 1:
        for _ in range(nums):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()



print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))