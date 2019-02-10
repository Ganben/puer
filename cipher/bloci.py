#!/usr/bin/python3
# -*- coding:utf-8 -*-
# a block cipher implement

class Cipher:

    def __init__(self, key):
        # build state bytes
        # key = bytearray, each 0-64, half char code
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
        
