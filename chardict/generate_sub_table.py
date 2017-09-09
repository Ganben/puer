#!/usr/bin/python3
# -*- coding:utf-8 -*-
# ganben
# generate two S-box from the frequency list
import os
import logging
import pickle
import codecs
import re

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

with codecs.open('./chardict/charfrequency.txt', encoding='utf-8') as f:
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