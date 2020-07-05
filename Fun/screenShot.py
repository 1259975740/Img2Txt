# -*- coding:utf-8 -*-  
import tkinter as tk
from tkinter import filedialog as fd
import os
from os import path
from PIL import ImageGrab
from time import sleep

class ScreenShot:
    def __init__(self,master,filename):
        
        self._createWidge(master, filename)
        #变量X和Y用来记录鼠标左键按下的位置
        
    def _onLeftButtonDown(self,event):
        self._X.set(event.x)
        self._Y.set(event.y)
        #开始截图
        self._sel = True
    
    def _onLeftButtonMove(self,event):
        if not self._sel:
            return
        try:
            #删除刚画完的图形，要不然鼠标移动的时候是黑乎乎的一片矩形
            self._canvas.delete(self._lastDraw)
        except Exception as e:
            pass
        self._lastDraw = self._canvas.create_rectangle(self._X.get(), self._Y.get(), 
                                                 event.x, event.y, outline='black',
                                                width = 5)

    def _onLeftButtonUp(self,event):
        self.fileName = os.path.join(os.path.dirname(__file__),'../Input') 
        self._sel = False
        try:
            self._canvas.delete(self._lastDraw)
        except Exception as e:
            pass
        sleep(0.1)
        #考虑鼠标左键从右下方按下而从左上方抬起的截图
        leftSel, rightSel = sorted([self._X.get(), event.x])
        topSel, bottomSel = sorted([self._Y.get(), event.y])
        pic = ImageGrab.grab((leftSel+1,topSel,rightSel+1,bottomSel))     
         #弹出保存截图对话框
        fDir = os.path.join(os.path.dirname(__file__),'../Input')  #���ϼ��ļ�Ŀ¼��
        self.fileName = fd.asksaveasfilename(title='保存截图',
                                        filetypes=[('JPG files','*.jpg')],
                                        initialdir=fDir)
        #默认的文件夹呀！！
        if self.fileName: 
            pic.save(self.fileName)
        pic.close()
        #关闭当前窗口
        #print(left, '  ', top,'  ',right,'  ',bottom)
        self.top.destroy()
        print(self.fileName)
        sleep(1)
        

    def _createWidge(self,master,filename):
        self.fileName =  os.path.abspath(os.path.join( os.path.dirname(__file__),".."))+'\Input'
        self._X = tk.IntVar(0)
        self._Y = tk.IntVar(0)
        
        #屏幕尺寸
        screenWidth = master.winfo_screenwidth()
        #print(screenWidth)
        screenHeight = master.winfo_screenheight()
        #print(screenHeight)
        #创建顶级组件容器
        self.top = tk.Toplevel(master, width=screenWidth, height=screenHeight)
        #不显示最大化、最小化按钮
        self.top.overrideredirect(True)
        self._canvas = tk.Canvas(self.top,bg='white', width=screenWidth, height=screenHeight)
        #显示全屏截图，在全屏截图上进行区域截图
        self._img = tk.PhotoImage(file=filename)
        self._canvas.create_image(screenWidth//2, screenHeight//2,image=self._img)
        #鼠标左键按下的位置
        self._canvas.bind('<Button-1>', self._onLeftButtonDown)
        #鼠标左键移动，显示选取的区域

        self._canvas.bind('<B1-Motion>', self._onLeftButtonMove)
        #获取鼠标左键抬起的位置，保存区域截图
            
        self._canvas.bind('<ButtonRelease-1>', self._onLeftButtonUp)
        self._canvas.pack(fill=tk.BOTH, expand=tk.YES)


def buttonCaptureClick(master):
    #最小化主窗口
    master.state('icon')
    sleep(0.5)
    filename = 'screenShot.png'
    im = ImageGrab.grab()
    im.save(filename)
    im.close()
    #显示全屏幕截图
    
    w = ScreenShot(master,filename)
#    master.printScrBut.wait_window(w.top)
    
    #截图结束，恢复主窗口，并删除临时的全屏幕截图文件
    #label.config(text='Hello')
    
    os.remove(filename)
    print(w.fileName)
    return w.fileName
