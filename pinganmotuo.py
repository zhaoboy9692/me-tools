from time import sleep

import requests


def tongzhi(ss):
   
    uids = [
        'UID_7Cq5Wq77cMJ',#通知uid
    ]
    for uid in uids:
        url = 'http://wxpusher.zjiecode.com/api/send/message/?appToken=AT_rNR6Rqp4BPOiHKc3G2oX11iJTv6TElej&content={}&uid={}'.format(
            ss, uid)
        r = requests.get(url)
        print(r.text)


headers = {
    'Host': 'newretail.pingan.com.cn',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 100000) MacWechat/32(0x1) MiniProgramEnv/Mac MiniProgram',
    'Referer': 'https://newretail.pingan.com.cn/ydt/newretail/',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
}
url = 'http://newretail.pingan.com.cn/ydt/booking/store/infos?pageNum=1&pageSize=100&cityCode=110100&source=miniApps&time=1686303213526'
index = 2000
while index > 0:
    res = requests.get(url, headers=headers)
    print(res.text)
    if '摩托' in res.text:
        tongzhi("平安摩托保险上了，快速预约！！！")
        break
    sleep(1)
