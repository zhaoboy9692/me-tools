#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 10:13:54
# @Author  : XinCheng.Zhao
# @Site    : 
# @File    : wxyd.py
# @Email   : zhaoboy9692@163.com


import hashlib
import json
import time
import requests


def run():
    account = '199692'  # 微信绑定得卓易账号
    step = '30561'  # 步数
    salt = '8061FD'
    time_stamp = str(int(time.time()))
    m = hashlib.md5()
    m.update(bytes(account + salt + time_stamp, encoding='utf8'))

    post_data = {
        'accountId': account,
        'timeStamp': time_stamp,
        'sign': m.hexdigest(),
    }
    res = requests.post('http://weixin.droi.com/health/phone/index.php/SendWechat/getWxOpenid', data=post_data)
    time_stamp = str(int(time.time()))
    if 'openid' not in str(res.text):
        print(json.loads(res.text)['messsage'])
        return
    openid = json.loads(res.text)['openid']
    m = hashlib.md5()
    m.update(bytes(account + salt + step + salt + time_stamp + salt + openid, encoding='utf8'))
    post_data = {
        'accountId': account,
        'timeStamp': time_stamp,
        'jibuNuber': step,
        'sign': m.hexdigest(),
    }
    res = requests.post('http://weixin.droi.com/health/phone/index.php/SendWechat/stepSubmit', data=post_data)
    print(json.loads(res.text)['messsage'])


if __name__ == '__main__':
    run()
