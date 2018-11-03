#!/usr/bin/python3
# -*- coding:utf-8 -*-
# ganben

import base64

def c_to_b64(c):
    #input char string utf8
    return base64.b64encode(c.encode('utf8'))

def b64_to_c(b):
    #input base64 string
    return base64.b64decode(b.decode('ascii'))