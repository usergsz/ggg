import os
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import torch
from torchvision import datasets, models, transforms
import torch.nn.functional as F
import torch.nn as nn
import time
import socket
from prediction import modelpre, showResult, remove_result

# 创建一个TCP客户端
socket_client = socket.socket()
host = "127.0.0.1"#"127.0.0.1"#
port = 2001
socket_client.connect((host,port))


# 主程序入口
if __name__ == "__main__":
    # 每次运行前清空上次运行识别结果缓存图片
    remove_result()    
    print('Waiting...')
    while True:
        data = socket_client.recv(1024).decode('utf-8')
        print(data)
        msg = ''
        if data == 'verify':
            src_roi = cv2.imread('D:/VisionMaster/image.jpg')
            # 将图像预处理后的图像进行模型推理
            label, pred_class = modelpre(src_roi)
            # 打印推理结果
            print(label, pred_class)
            # 显示推理结果
            showResult(src_roi, pred_class)
            if label == 0:
                msg = 'fanghufu'
            elif  label == 1:
                msg = 'kouzhao'
            elif label == 2:
                msg = 'kuangquanshui'
            elif  label == 3:
                msg = 'mianbao'
            elif label == 4:
                msg = 'xiangchang'
            elif label == 5:
                msg = 'yiyongshoutao'   
            socket_client.send(msg.encode())
            data = ''
        else:
            msg = 'null'
            socket_client.send(msg.encode())
            print('data error!')
         

