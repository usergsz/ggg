from tkinter import *
import time
#import socket
import numpy as np
from FaceRecognition import Face
from PIL import Image, ImageTk 
import cv2#导入opencv库
import matplotlib
import os
#matplotlib.use('Agg')   #该模式下绘图无法显示，plt.show()也无法作用
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import socket
import threading
# 创建socket客户端变量
socket_client = ''
#创建全局变量
global command
socket_client = socket.socket()
socket_client.connect(('127.0.0.1', 2001))
#二维码接收函数
def code_loop():
    while(True):
        command = socket_client.recv(1024).decode()
        print('')
        print(command)
        if command == 'code':
            print("getcode")

#人脸图片显示函数，所有的人脸图片显示的时候可以加载这个函数
def face_image(face_photo):
    global photo1 #一定要将photo设置成全局变量不然调用显示不出来 image
    photo_open1 = Image.open('./' + face_photo + '.jpg') #打开图片
    photo1 = photo_open1.resize((120 , 120))  #图片尺寸
    photo1 = ImageTk.PhotoImage(photo1)   
    Label(Frame1,image=photo1).place(x= 50,y = 80) # 放置人脸图像的标签及位置

#二维码图片显示函数，所有的二维码图片显示的时候可以加载这个函数
def code_image(code_photo):
    global photo2 #一定要将photo设置成全局变量不然调用显示不出来 
    #初始化的图片使用PIL库来加载图像
    photo_open2 = Image.open('./' + code_photo + '.jpg') #打开图片
    photo2 = photo_open2.resize((100 , 100))  #图片尺寸
    photo2 = ImageTk.PhotoImage(photo2)  # 放置二维码图像的标签及位置
    Label(Frame2,image=photo2).place(x= 50,y = 100) # 放置人脸图像  

#人脸登录函数。function：face_login
def face_login():
    print("人脸登录")
    name,face_id = Face() #采集人脸数据
    print(name,face_id )
    Label(Frame1,text = face_id , font = ("微软雅黑",15), fg = "LightSlateGray" , bg = "White").place(x= 280,y = 100)  # ID
    Label(Frame1,text = name , font = ("微软雅黑",15), fg = "LightSlateGray", bg = "White").place(x= 280,y = 150)  # 姓名  
    Label(Frame1,text = "登录成功！" , font = ("微软雅黑",20), fg = "lawngreen" , bg = "White").place(x= 150,y = 220) 
    face_image('image')

#注销函数。function：face_logout
def face_logout():
    print('人脸登出')
    Label(Frame1,text = "     " , font = ("微软雅黑",15), fg = "LightSlateGray" , bg = "White").place(x= 280,y = 100)  # 用空格顶掉原有的信息
    Label(Frame1,text = "      " , font = ("微软雅黑",15), fg = "LightSlateGray", bg = "White").place(x= 280,y = 150)  # 用空格顶掉原有的信息
    Label(Frame1,text = "              " , font = ("微软雅黑",20), fg = "lawngreen" , bg = "White").place(x= 150,y = 220) 
    global photo1 #一定要将photo设置成全局变量不然调用显示不出来 
    face_image('face')

#二维码识别，识别的是视觉拍摄的code.jpg    
def code_recognition():
    #根据视觉是否对二维码拍照判断，若拍照了，则文件夹内有code.jpg
    if os.path.exists("./code.jpg"):
        
        img = cv2.imread("./code.jpg")#打开二维码图片
        det = cv2.QRCodeDetector()#创建二维码识别器
        val, pts, st_code = det.detectAndDecode(img)#识别二维码
        #print(val)
        return val
    else:       
        val = "0 0 0 0"  #文件夹内没有code.jpg,则返回code0.jpg的二维码信息
        return val

#画扇形图
def draw_pie(frame,labels,fraces):
    # Figure创建图像对象，figsize指定画布的大小，(宽度,高度)，单位为英寸。
    # dpi 指定绘图对象的分辨率，即每英寸多少个像素，默认值为80
    fig = Figure(figsize=(4, 4), dpi=100)
    # 把绘制的图形显示到tkinter窗口上
    canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea.
    canvas.get_tk_widget().place(x=200,y=100) #把控件放到tk
    # subplot()均等划分画布,如果不想覆盖之前的图，需要使用 add_subplot() 函数
    drawPic_a = fig.add_subplot(111)
    # 解决汉字乱码问题，使用指定的汉字字体类型（此处为黑体）
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']  
    #颜色
    colors = ["LawnGreen" ,"DodgerBlue","Yellow","red"]
    # 绘制pie()饼状图：labels为每个扇形区域备注一个标签名字,autopct格式化字符串"fmt%pct",百分比格式
    drawPic_a.pie(x=fraces, labels=labels, colors = colors , autopct='%0.2f%%') 
    drawPic_a.set_title('风险区分布图')  #饼状图命名
    canvas.draw()  #加载到画布

#主程序入口
if __name__ == '__main__':
    #风险区划分（具体划分还需要详细说明）：#低风险除了中、隔离的都是低，低风险可去掉
    risk = {"低风险":{"深圳光明","汕头濠江","广州从化","珠海香洲","福建厦门"}, 
            "中风险":{"上海浦东","上海崇明","上海宝山","上海普陀","上海金山"},
            "高风险":{"河南郑州","河南金水","河南高新","深圳福田","深圳宝安"},
            "隔离区":{"内蒙古呼和浩特","内蒙古呼伦贝尔","内蒙古赤峰","内蒙古包头"}}
    #二维码人员信息初始值:姓名（用于判断）
    code_name = "0"

    #识别总人数sum
    sum = 0
    #低风险人数
    low = 0
    #中风险人数
    mid = 0
    #高风险人数
    hight = 0
    #隔离区人数
    quarantine = 0

    #人脸训练集路径
    path = './Facedata/'
    #主界面程序
    top = Tk()
    top.title("越疆科技")  # 窗口标题
    top.geometry("1200x700")  # 窗口尺寸
    top.configure(bg = "Navy")  # 窗口背景颜色
    #大标题"机场人员流调系统"
    Label(top ,text = "机场人员流调系统",font = ("宋体",18),fg = "White",bg = "Navy",width = 30,height = 2).place(x=420,y = 0)
    
    #设置3个Frame框架组件，用来存放人脸识别、人员信息、风险布局
    #第一个框架：人脸登录、注销
    Frame1 = Frame(top,bg="White",height=280,width=400)
    Frame1.place(x = 50 , y = 50)
    Button(Frame1,text = "人脸登录",bg = "LightSeaGreen",font = ("黑体",12),width = 10,height = 2,command = face_login).place(x = 80 , y = 10)  #人脸登出按钮
    Button(Frame1,text = "注销",bg = "Gold",font = ("黑体",12),width = 10 , height = 2,command = face_logout).place(x= 230,y = 10)   #注销按钮
    #第一个框架：人脸登录、注销
    face_image('face')  #初始化人脸图像
    Label(Frame1,text = "Face ID:",font = ("微软雅黑",15), bg = "White" , width = 10 , height = 1).place(x= 170,y = 100)  # ID
    Label(Frame1,text = "  Name:",font = ("微软雅黑",15), bg = "White" , width = 10 , height = 1).place(x= 170,y = 150)  # 姓名

    #第二个框架：人员信息识别
    Frame2 = Frame(top,bg="White",height=280,width=400)
    Frame2.place(x = 50 , y = 380)
    Label(Frame2,text = "人员信息识别",font = ("微软雅黑",15), bg = "White" , width = 10 , height = 1).place(x= 130,y = 10)  # 姓名
    #第二个框架：人员信息识别
    code_image("code0")

    #第三个框架：人员信息识别 
    Frame3 = Frame(top,bg="White",height=610,width=650)
    Frame3.place(x = 500 , y = 50)

    thread = threading.Thread(target=code_loop)
    thread.daemon = True
    thread.start()

    while(True):
        time.sleep(0.5)
        #每隔1ms刷新一次界面 
        top.update()
        top.after(1) 
        #检测二维码是否更新
        while(True): 
            fraces = []
            labels_list = []
            #检测原来的姓名与二维码图片中的姓名是否一致,code_name初始值为0
            if code_name == code_recognition().split(' ')[0]:  # 调用二维码识别，转为列表，对结果字符串分割
                code_list  = code_recognition().split(' ')  #获取二维码中的数据
                break  #姓名一致说明图片没换，跳出循环
            else:  #姓名不一致，新人员！！
                code_list  = code_recognition().split(' ')  #获取新的二维码中的数据
                code_name = code_recognition().split(' ')[0]  #赋值用于判断
                code_image("code")
 
                sum += 1  #识别人数+1
                area = code_list[3]
                for k,v in risk.items():     
                    if area in v:
                        print(k)
                        if k == "低风险": low += 1
                        if k == "中风险": mid += 1
                        if k == "高风险": hight += 1
                        if k == "隔离区": quarantine += 1
                        #将风险区和对应值组合成字典
                        risk_dict = {"低风险" : low , "中风险" : mid , "高风险" : hight , "隔离区" : quarantine }
                        
                        for i in list(risk_dict.keys()):  #改为一个list（非迭代器）
                            if risk_dict[i]== 0:
                                print(type(risk_dict[i]))
                                del risk_dict[i]  #删除键值为“0”的键和对应键值
                                continue
                        print("risk_dict:",risk_dict) 
                        #将键值以列表形式拼接起来，作为扇形图的占fraces；同理键也已列表形式拼接起来为不同风险区labels_list                  
                        for k,v in risk_dict.items():  #遍历最终的字典
                            fraces.append(v)    #[1,2,3,4]    
                            labels_list.append(k)  # ["低风险","中风险","高风险","隔离区"]            
                        labels = tuple(labels_list)   # 转为元组  labels = ("低风险","中风险","高风险","隔离区") 
                        print("labels:",labels)  
                draw_pie(Frame3,labels,fraces)  # 画扇形图
                break
        #初始为空
        if code_list[0] == "0":  
            code_list[0] = code_list[1] = code_list[2] = code_list[3]= ' '
          
         
        Label(Frame2,text = "姓名: " + code_list[0],font = ("微软雅黑",15), bg = "White" , width = 15 , height = 1 , anchor = 'w' ).place(x= 170,y = 80)  # 姓名
        Label(Frame2,text = "性别: " + code_list[1],font = ("微软雅黑",15), bg = "White" , width = 15 , height = 1, anchor = 'w' ).place(x= 170,y = 120)  # 性别
        Label(Frame2,text = "年龄: " + code_list[2],font = ("微软雅黑",15), bg = "White" , width = 15 , height = 1, anchor = 'w' ).place(x= 170,y = 160)  # 年龄
        Label(Frame2,text = "行程: " + code_list[3],font = ("微软雅黑",15), bg = "White" , width = 15 , height = 1, anchor = 'w' ).place(x= 170,y = 200)  # 行程 
        #第三个框架：人员信息识别 
        Label(Frame3,text = "识别总人数: " + str(sum) + "个" , font = ("微软雅黑",12), bg = "Gray" , width = 15 , height = 2).place(x= 50,y = 70)  
        Label(Frame3,text = "低风险人数: " + str(low) + "个" , font = ("微软雅黑",12), bg = "LawnGreen" , width = 15 , height = 2).place(x= 50,y = 170)  
        Label(Frame3,text = "中风险人数: " + str(mid) + "个" , font = ("微软雅黑",12), bg = "DodgerBlue" , width = 15 , height = 2).place(x= 50,y = 270)  
        Label(Frame3,text = "高风险人数: " + str(hight) +"个" , font = ("微软雅黑",12), bg = "Yellow" , width = 15 , height = 2).place(x= 50,y = 370) 
        Label(Frame3,text = "隔离区人数: " + str(quarantine) + "个" , font = ("微软雅黑",12), bg = "red" , width = 15 , height = 2).place(x= 50,y = 470) 
     

