#!/usr/bin/python3
# -*- coding:utf-8 -*-
# ganben
# generate two S-box from the frequency list
import os
import logging
import pickle
import codecs
import re
import os
import unittest

script_dir = os.path.dirname(__file__)

log = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
log.addHandler(ch)
# set formatters,
# set logging levels, etc
log.setLevel(logging.INFO)
filepath = os.path.join(script_dir, 'charfrequency.txt')
with codecs.open(filepath, encoding='utf-8') as f:
    content = f.readlines()
# source: Jun Da 笪骏 (jda@mtsu.edu) http://lingua.mtsu.edu/chinese-computing/statistics/char/list.php?Which=TO
log.debug('len %s read' % len(content))
count = 0
charlist = []
digit_re = re.compile('\A(\d+?)\s')
split_re = re.compile('(.+?)\s')

for line in content:
    log.debug('line: %s' % line)
    # print(digit_re.findall(line))
    li = split_re.split(line)
    log.debug('list len %s' % li[3] )
    charlist.append(li[3])
long_dict_ctn = {}
n=64
m=64
# use generators
ntc_array = [['一'] * m for i in range(n)]

for i in range(0,64):
    for j in range(0,64):
        index = j * 64 + i
        char = charlist[index]
        ntc_array[j][i] = char
        ns = (j,i)
        long_dict_ctn[char] = ns
        log.debug('%s=%s,%s' % (char, j, i))

#with open( "long_dict_ctn.p", "wb" ) as f1:
#    pickle.dump(long_dict_ctn, f1)

#with open('ntc_array.p', 'wb') as f2:
#    pickle.dump(ntc_array, f2)

cn1 = 32
cn2 = 19
char = ntc_array[cn1][cn2]
num = long_dict_ctn.get(char)

log.debug('%s:%s-%s' % (ntc_array[cn1][cn2], num[0], num[1]))

def get_long_dict():
    return long_dict_ctn

def get_ntc_array():
    return ntc_array


def save_to_file():
    lines = []
    for k,v in long_dict_ctn.items():
        lines.append('%s,%d,%d\n' % (k, v[0], v[1]))
    filepath = os.path.join(script_dir, 'chartable.csv')
    with open(filepath, 'w') as f:
        f.writelines(lines)
    filepath2 = os.path.join(script_dir, 'chartable_utf8.csv')
    with codecs.open(filepath2,'w',encoding='utf8') as f:
        f.writelines(lines)
    return True

def save_ctn():
    lines = []
    for i in range(0,64):
        line = []
        for j in range(0,64):
            line.append("%s" % ntc_array[i][j])
        lines.append(','.join(line)+'\n')
    filepath = os.path.join(script_dir, 'ctnarray.csv')
    with open(filepath, 'w') as f:
        f.writelines(lines)
    
    filepath2 = os.path.join(script_dir, 'ctnarray_utf8.csv')
    with codecs.open(filepath2,'w',encoding='utf8') as f:
        f.writelines(lines)

def save_to_file2():
    lines = []
    for k,v in long_dict_ctn.items():
        lines.append('\'%s\',%d,%d\n' % (k, v[0], v[1]))
    filepath = os.path.join(script_dir, 'chartable2.csv')
    with open(filepath, 'w') as f:
        f.writelines(lines)
    filepath2 = os.path.join(script_dir, 'chartable_utf82.csv')
    with codecs.open(filepath2,'w',encoding='utf8') as f:
        f.writelines(lines)
    return True

def save_to_java():
    lines = []
    for k,v in long_dict_ctn.items():
        lines.append('{%d,%d},\n' % (v[0], v[1]))
    filepath = os.path.join(script_dir, 'chartable_java_int.csv')
    with codecs.open(filepath,'w',encoding='utf8') as f:
        f.writelines(lines)
    lines2 = []
    for k,v in long_dict_ctn.items():
        lines2.append('\'%s\',\n' % k)
    filepath = os.path.join(script_dir, 'chartable_java_char.csv')
    with codecs.open(filepath,'w',encoding='utf8') as f:
        f.writelines(lines2)
    

def save_ctn2():
    lines = []
    for i in range(0,64):
        line = []
        for j in range(0,64):
            line.append("\'%s\'" % ntc_array[i][j])
        lines.append(','.join(line)+'\n')
    filepath = os.path.join(script_dir, 'ctnarray2.csv')
    with open(filepath, 'w') as f:
        f.writelines(lines)
    
    filepath2 = os.path.join(script_dir, 'ctnarray_utf82.csv')
    with codecs.open(filepath2,'w',encoding='utf8') as f:
        f.writelines(lines)

    return filepath

class Test1(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(save_to_file())
    def test2(self):
        self.assertIsNotNone(save_ctn())