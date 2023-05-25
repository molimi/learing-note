"""
Version: 0.1
Author: CarpeDiem
Date: 2023/5/12
Description: 
思路：智能聊天
"""
import hashlib
import urllib
from urllib import parse
import urllib.request
import json
import time
import itchat

#腾讯智能闲聊接口
#api接口的链接
url_preffix='https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'
# 因为接口相应参数有要求，一开始是=我是封装在模块里的，但为了大家方便，就整合到了一起
def setParams(array, key, value):
    array[key] = value
# 生成接口的sign签名信息方法，接口参数需要 可参考：https://ai.qq.com/doc/auth.shtml 


def genSignString(parser):
    uri_str = ''
    for key in sorted(parser.keys()):
        if key == 'app_key':
            continue
        uri_str += "%s=%s&" % (key, parse.quote(str(parser[key]), safe=''))
    sign_str = uri_str + 'app_key=' + parser['app_key']

    hash_md5 = hashlib.md5(sign_str.encode('utf-8'))
    return hash_md5.hexdigest().upper()


class AiPlat(object):
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key
        self.data = {}
        self.url_data = ''
    #调用接口并返回内容


    def invoke(self, params):
        self.url_data = urllib.parse.urlencode(params).encode("utf-8")
        req = urllib.request.Request(self.url, self.url_data)
        try:
            rsp = urllib.request.urlopen(req)
            str_rsp = rsp.read().decode('utf-8')
            dict_rsp = json.loads(str_rsp)
            return dict_rsp
        except Exception as e:
            print(e)
            return {'ret': -1}
        #此方法生成为api接口准备串接所需的请求参数

    def Messagela(self,question):
        self.url = url_preffix
        setParams(self.data, 'app_id', self.app_id)#应用标识
        setParams(self.data, 'app_key', self.app_key)   
        setParams(self.data, 'time_stamp', int(time.time()))#时间戳
        setParams(self.data, 'nonce_str', int(time.time()))#随机字符串
        setParams(self.data, 'question', question)#聊天内容
        setParams(self.data, 'session', '135248')#session
        sign_str = genSignString(self.data)
        setParams(self.data, 'sign', sign_str)#签名
        return self.invoke(self.data)

"""至此上面的部分就是通过腾讯AL获取聊天恢复内容,有些麻烦，之前是封装起来的，这里写在一起，方便你们看一下"""
# appid: 2138952940
#APPKEY:BmpKFOHjDXW89ReW
# 这是我自己申请的，大家可以随意使用，也可自行去ai.qq.com注册
def getmessage(messageall):
        try:
            Message=AiPlat('2138952940', 'BmpKFOHjDXW89ReW')
            response=Message.Messagela(messageall)
            return response['data']['answer']           
        except Exception as ex :
            print(ex)
            print("你是不是有什么库没安装啊")

@itchat.msg_register(itchat.content.TEXT)   # 微信聊天信息监听存放在msg[]里，当然也监听map picture,等内容，可自行了解itchat.

def tencent_reply(msg):
    # 设置一个默认回复，在出现问题仍能正常回复信息
    defaultReply = '我没理解你的意思' + msg['Text']
    reply = getmessage(msg['Text'])
    # a or b 表示，如有a有内容，那么返回a，否则返回b
    return reply or defaultReply

#主程序
# 使用热启动，不需要多次扫码
'''如启动失败，可将hotReload=True删掉，这是热启动，再次启动时无需在次扫码，具体情况自行考虑'''
itchat.auto_login(hotReload=True)#hotReload=True
itchat.run()
