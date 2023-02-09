#!/usr/bin/env python3
# -*- coding: utf-8 -*-
new_string = ""
with open("./String.txt", 'r') as fs:
    for line in fs:
        for ch in line:
            if ch.isdigit():
                new_string += ch
print(new_string)
