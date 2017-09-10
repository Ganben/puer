#!/usr/bin/python3
# -*- coding:utf-8 -*-
# ganben:

import puer.chardict.chardict as chardict
import puer.cipher.cipher as cipher


def encrypt(key, text):
    text, sii = chardict.text_to_intint(text)
    key = bytearray(key, 'chinese')
    key = key + b' ' * 16
    key = key[:16]
    ecr = cipher.encrypt(text, key)
    ecr = chardict.join_text(ecr, sii)

    return ecr


def decrypt(key, text):
    chars, sii = chardict.text_to_intint(text)
    key = bytearray(key, 'chinese')
    key = key + b' ' * 16
    key = key[:16]
    dcr = cipher.decrypt(chars, key)
    dcr = chardict.join_text(dcr, sii)

    return dcr

def kengen(seed=None):
    sk, vk = cipher.generate_keypair()
    return (chardict.join_text(sk), chardict.join_text(vk))

def sign(key, msg):
    key, _ = chardict.text_to_intint(key)
    aii, _ = chardict.text_to_intint(msg)
    signature = cipher.sign_message(key, aii)

    return chardict.join_text(signature)

def verify(key, msg, sig):
    key, _ = chardict.text_to_intint(key)
    sig, _ = chardict.text_to_intint(sig)
    text, _ = chardict.text_to_intint(msg)
    res = cipher.verify_message(key, sig, msg)

    return res