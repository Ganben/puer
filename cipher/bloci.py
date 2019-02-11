#!/usr/bin/python3
# -*- coding:utf-8 -*-
# a block cipher implement
import unittest
import random

class Cipher:

    def __init__(self, key):
        # build state bytes
        # key = bytearray, each 0-64, half char code/ not, it is a int array 2n ele
        self.key = key
        self.state = bytearray(64)
        self.init_state()
        self.pi = 0
        self.pj = 0 # init for pRGA flagger


    def init_state(self):
        # refs: Key-scheduling algorithm (KSA)
        for i in range(64):
            self.state[i] = i
        
        j = 0
        for i in range(64):
            j = (j + self.state[i] + self.key[i % len(self.key)]) % 64
            swap = self.state[j]
            self.state[j] = self.state[i]
            self.state[i] = swap
        return
    
    def pseudo_random(self):
        self.pi = (self.pi + 1) % 64
        self.pj = (self.pj + self.state[self.pi]) % 64
        swap = self.state[j]
        self.state[j] = self.state[i]
        self.state[i] = swap
        ret = self.state[(self.state[self.pi] + self.state[self.pj]) % 64 ]
        return ret
        
    def encrypt(self, content):
        # content is a bytearray or int array 2n ele
        # the position based pseudo_random plus output's mod
        output = []
        op_mod = [0]
        for el in content:
            output_e = el ^ self.pseudo_random() ^ op_mod[-1]
            op_mod_e = (output_e + el) % 64
            output.append(output_e)
            op_mod.append(op_mod_e)
        return output

    def decrypt(self, content):
        # content is a bytearray or int array 2n ele
        output = []
        op_mod = [0]
        for el in content:
            output_e = el ^ self.pseudo_random() ^ op_mod[-1]
            op_mod_e = (output_e + el) % 64
            output.append(output_e)
            op_mod.append(op_mod_e)
        return output


class Test(unittest.TestCase):
    def t1(self):
        o = Cipher([62,60,0,1,0,27])
        c = []
        for i in range(100):
            c.append(random.randint(0,63))
        e = o.encrypt(c)
        self.assertListEqual(c, o.decrypt(e))
        