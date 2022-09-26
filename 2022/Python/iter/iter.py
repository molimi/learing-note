"""
Version: 0.1
Author: CarpeDiem
Date: 2022/5/2
Description: 可迭代对象
"""
from typing import Iterable
import os.path

print(isinstance([], Iterable))  # True list是可迭代对象
print(isinstance({}, Iterable))  # True dict是可迭代对象
print(isinstance((), Iterable))  # True tuple是可迭代对象
print(isinstance(set(), Iterable))  # True set是可迭代对象
print(isinstance('', Iterable))  # True string是可迭代对象
Current_Path = os.path.dirname(os.path.abspath(__file__))
with open(Current_Path + '/iter.py') as file:
    print(isinstance(file, Iterable))  # True
