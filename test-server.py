#!/usr/bin/python3
# -*- coding:utf-8 -*-
# ganben: test async call and cache test
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import jsonify

import chardict.chardict as chardict
import cipher.cipher as cipher

import logging

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        text, sii = chardict.text_to_intint(text)
        key = bytearray(key, 'chinese')
        key = key + b' '*16
        key = key[:16]
        ecr = cipher.encrypt(text, key)
        ecr = chardict.join_text(ecr, sii)
        return ecr

    else:
        return '''
            <p>Encrypt Weibo post</p>
            <form method="post">
            <p><textarea cols=40 rows=10 name=text style="background-color:BFCEDC"></textarea>
            <p><input type=text name=key value='ENCRYPT KEY(8)'>
            <p><input type=submit value=TEST>
        </form>
        '''


@app.route('/encrypt', methods=['POST'])
def encrypt():
    """only for api call"""
    try:
        text = request.form['text']
        key = request.form['key']
    except:
        return jsonify({'error': 'no data'})

    if 0 < len(text) < 200 and 0 < len(key)<8:
        # chars = ts.filterchars(text)
        # keychar = ts.filterchars(key)
        chars, sii = chardict.text_to_intint(text)
        key = bytearray(key, 'chinese')
        key = key + b' '*16
        key = key[:16]

        if len(chars)>0 and len(key) >0:
           # ecr = ts.encryptext(chars, keychar)
           ecr = cipher.encrypt(chars, key)
           ecr = chardict.join_text(ecr, sii)

           return '%s \n%s' % (key, ecr)
        else:
            return jsonify({'error': 'no valid chars'})


    else:
        return jsonify({'error': 'too long text or key'})



@app.route('/dec', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        # _ = ts.update(text)
        # _ = ts.update(key)
        chars, sii = chardict.text_to_intint(text)
        key = bytearray(key, 'chinese')
        key = key + b' ' * 16
        key = key[:16]
        dcr = cipher.decrypt(chars, key)
        dcr = chardict.join_text(dcr, sii)

        return dcr

    else:
        return '''
            <p>Encrypt Weibo post</p>
            <form method="post">
            <p><textarea cols=40 rows=10 name=text style="background-color:BFCEDC"></textarea>
            <p><input type=text name=key value='DECRYPT KEY(8)'>
            <p><input type=submit value=TEST>
        </form>
        '''

@app.route('/keygen', methods=['GET'])
def keygen():
    sk, vk = cipher.generate_keypair()
    return '%s\n%s' % (chardict.join_text(sk), chardict.join_text(vk))


@app.route('/keysign', methods=['GET', 'POST'])
def keysign():
    if request.method == 'POST':
        key = request.form['key']
        # key = bytearray(key, 'chinese')
        key, _ = chardict.text_to_intint(key)
        text = request.form['text']
        aii, _ = chardict.text_to_intint(text)
        signature = cipher.sign_message(key, aii)
        return chardict.join_text(signature)

    else:
        return '''
            <p>Signing with Key</p>
            <form method="post">
            <p><textarea cols=40 rows=10 name=text style="background-color:BFCEDC"></textarea>
            <p><input type=text name=key value='SKEY'>
            <p><input type=submit value=Sign>
        </form>
        '''


@app.route('/sigverify', methods=['GET', 'POST'])
def sigverify():
    if request.method == 'POST':
        key = request.form['key']
        # key = bytearray(key, 'chinese')
        key, _ = chardict.text_to_intint(key)
        sig = request.form['sig']
        sig, _ = chardict.text_to_intint(sig)
        text = request.form['text']
        text, _ = chardict.text_to_intint(text)
        res = cipher.verify_message(key, sig, text)
        return jsonify({'result': res})
    else:
        return '''
            <p>Verify with Key</p>
            <form method="post">
            <p><textarea cols=40 rows=10 name=text style="background-color:BFCEDC"></textarea>
            <p><input type=text name=key value='VKEY'>
            <p><input type=text name=sig value='SIG'>
            <p><input type=submit value=Verify>
        </form>
        '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)