#!/usr/bin/python3
# -*- coding:utf-8 -*-
# ganben
# entrancy func of char dict utilities

import chardict.generate_sub_table as ge




long_dict_ctn = ge.get_long_dict()
ntc_array = ge.get_ntc_array()


def trans_code(scch):
    """
    look up the table and return changed code;
    :param scch: '喊'
    :return: ord int
    """
    u = long_dict_ctn.get(scch)
    if u:
        return u
    else:
        return None


def reverse_code(cycode):
    """
    look up the reverse table and return original unicode
    :param cycode:   (64,64)
    :return:  '喊'
    """
    if cycode[0] in range(0,64) and cycode[1] in range(0,64):
        return ntc_array[cycode[0]][cycode[1]]
    else:
        return None


def text_to_intint(text):
    """
    the non char will be replaced with ,
    :param text: 'char'
    :return: ([(int,int)], non-char seq[(pos, [])])
    """
    pass


def join_text(aii, sii):
    """
    join the split two seq to text
    :param aii: [(int,int)]
    :param sii: [(int, str)]
    :return: text str
    """
    pass
