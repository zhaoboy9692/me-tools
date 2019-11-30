#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2019-11-30 13:29
@Author  : Xincheng.Zhao
@Desc    :
@Email   : zhaoboy9692@163.com
@File    : imei.py
"""


def genImeiLuhn(digits14):
    digit15 = 0
    digits14 = str(digits14)
    for num in range(14):
        if num % 2 == 0:
            digit15 = digit15 + int(str(digits14)[num])
        else:
            digit15 = digit15 + (int(digits14[num]) * 2) % 10 + (int(digits14[num]) * 2) / 10
    digit15 = int(digit15) % 10
    if digit15 == 0:
        digits14 = digits14 + str(digit15)
    else:
        digits14 = digits14 + str(10 - digit15)
    return digits14


def genMassImei(stat14digits, amount, filepath):
    fo = open(filepath, "a+")
    for num in range(amount):
        imei = genImeiLuhn(stat14digits)
        stat14digits = str(int(stat14digits) + 1)
        fo.write(imei + "\n")
        print(imei)
    fo.flush()
    fo.close()


genMassImei(142430023100009, 1000, "imei2.txt")
