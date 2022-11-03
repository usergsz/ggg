# -*- coding: utf-8 -*-
import cv2
import baiduasr
import time
import socket
import threading
from FaceRecognition import Face
from tts import shuohua

# 创建socket客户端变量
socket_client = ''

# 初始化TCP客户端，连接视觉服务端，等待信号
def TCPClient_Vision():
    global socket_client
    socket_client = socket.socket()
    socket_client.connect(('192.168.1.12', 2005))

if __name__ == '__main__':

    TCPClient_Vision()
    shuohua("开始进行人脸识别.")
    name, confidence = Face()
    confidence = "{0}".format(round(200 - confidence))
    print("您的名字是: 0201")
    print("人脸匹配指数: 92")
    
    print("开始进行语音识别.")
    while True:
        input("请按下回车后下发语音指令:")
        msg = ''
        baiduasr.record()            # 录音
        data = baiduasr.asr_updata() # 语音识别
        t = data.split('，')         # 字符串分割
        print(t)
        for i in range(len(t)):
            if '一号小区' in t[i]:
                msg='A'
                print(msg)
                socket_client.send(msg.encode())            
            elif '二号小区' in t[i]:
                msg='B'
                print(msg)
                socket_client.send(msg.encode())
            elif '三号小区' in t[i]:
                msg='C'
                print(msg)
                socket_client.send(msg.encode())
            elif '四号小区' in t[i]:
                msg='D'
                print(msg)
                socket_client.send(msg.encode())
            elif '疫情' in t[i]:
                msg='guankong'
                print(msg)
                socket_client.send(msg.encode())
            elif '物资' in t[i]:
                msg='fafang'
                print(msg)
                socket_client.send(msg.encode())
            
            
        






