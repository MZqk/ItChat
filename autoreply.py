#coding=utf8
import requests
import itchat
from itchat.content import *

KEY = '2f51a52995884edeba33e18477bf69bc'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return
def enter():
    itchat.send(msg='login successful',toUserName='filehelper')

@itchat.msg_register(TEXT)
def text_reply(msg):
    defaultReply = 'I received your say: ' + msg['Text']
    reply = get_response(msg['Text'])
    print('RE:'+msg['Text'])
    print("SE:"+reply)
    return reply or defaultReply

@itchat.msg_register(PICTURE)
def pic_reply(msg):
    print('get a pic ')
    itchat.send_image('reply.png',toUserName=None)

itchat.auto_login(enableCmdQR=True,loginCallback=enter)
itchat.run()
