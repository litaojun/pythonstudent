#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月11日

@author: ｌｉｔａｏｊｕｎ
'''
import rsa
#from Config import config
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(1024)
pubkey = key.publickey().key
def Decrypt(prikey,data):
                try:
                        cipher = PKCS1_OAEP.new(prikey, hashAlgo=SHA256)
                        return cipher.decrypt(data)
                except:
                        #traceback.print_exc()
                        return None

def Encrypt(pubkey,data):
                try:
                        cipher = PKCS1_OAEP.new(pubkey, hashAlgo=SHA256)
                        return cipher.encrypt(data)
                except:
                        #traceback.print_exc()
                        return None
if __name__ == '__main__':
    pass