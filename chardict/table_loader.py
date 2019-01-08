#!/usr/bin/python3
# -*- coding:utf-8 -*-
# ganben

import os
import logging
import pickle
import codecs
import re
import os
import unittest

script_dir = os.path.dirname(__file__)

filepath = os.path.join(script_dir, 'chartable.csv')
with codecs.open(filepath) as f:
    content = f.readlines()

long_dict_ctn = {}
ntc_array = [[''] * 64 for i in range(64)]

for s in content:
    char = s.split(',')
    long_dict_ctn[char[0]] = (int(char[1]), int(char[2].rstrip()))

filepath = os.path.join(script_dir, 'ctnarray.csv')
with codecs.open(filepath) as f:
    content = f.readlines()

ntc_array_n = []
for s in content:
    ele = s.split(',')
    ele[-1] = ele[-1].rstrip()
    ntc_array_n.append(ele)

def get_long_dict():
    return long_dict_ctn

def get_ntc_array():
    return ntc_array_n




#print(char[2].rstrip())
