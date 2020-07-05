# coding: utf-8
import tkinter as tk
from tkinter import ttk
import os
from os import path
from tkinter import filedialog as fd
import sys
from threading import Thread
from Tooltip import createToolTip
sys.path.append('../')
from Fun.pdf2txt import trans


class Tab2():
    def __init__(self,tab,i18n):
        self._createWidget(tab,i18n)
    def _getIptFileName(self):
        fDir = os.path.join( os.path.dirname(__file__),'..\Input')
        fName = fd.askopenfilename(parent=self.inOutFrm,initialdir=fDir)
        fPath = path.dirname(fName)
        self.inEry.delete(0,tk.END)   
        self.inEry.insert(0,fName)   
        
    def _getOptFileName(self):
        fDir = os.path.join( os.path.dirname(__file__),'..\Output')  
        fName = fd.askdirectory(parent=self.inOutFrm,initialdir=fDir)
        fPath = path.dirname(fName)
        self.outEry.delete(0,tk.END)   
        self.outEry.insert(0,fName)  
        
    
    def _createTransThread(self):
        
        input_file = r''+self.inEry.get()
        files = []
        files.append(input_file)
        output_file = self.outEry.get() 
        print(input_file)
        run = Thread(target=trans,args=(files,output_file))
        run.setDaemon(True)
        run.start()
    
    def _trans(self):
        self._createTransThread()
    
        
    def _createWidget(self,tab,i18n):
        self.zhuo = ttk.Frame(tab)
        self.zhuo.grid(row=0,column=0)
                # 文件管理栏目
        self.inOutFrm = ttk.Frame(self.zhuo)
        self.inOutFrm.grid(column=0,row=0,sticky='W')
        
        self.inBut = ttk.Button(self.inOutFrm,text=i18n.inButTab2,
                            command=self._getIptFileName)
        self.inBut.grid(column=0,row=0)
        self.inEry = ttk.Entry(self.inOutFrm,width=60)
        self.inEry.grid(column=1,row=0)
        
        self.outBut = ttk.Button(self.inOutFrm,text=i18n.outBut,
                                 command=self._getOptFileName)
        self.outBut.grid(column=0,row=1)
        self.outEry = ttk.Entry(self.inOutFrm,width=60)
        self.outEry.grid(column=1,row=1)
        
        createToolTip(self.outEry,'输入文件名称，包括后缀。后缀可以是 html、txt、xml。文件可以不必存在于磁盘中，代码会帮助你自动创建文件')    #给控件 aScrTxt 绑定一个提示框。
        
        for child in self.inOutFrm.winfo_children():
            child.grid_configure(padx=6,pady=6,sticky='W')
        
        
        
        #转换按钮
        self.butFrm = ttk.Frame(self.zhuo)
        self.butFrm.grid(column=0,row=2,sticky='W',pady=6)

        self.transBut = ttk.Button(self.butFrm,text=i18n.transBut,
                                   command=self._trans)
        self.transBut.grid(column=1,row=0)
        
        for child in self.butFrm.winfo_children():
            child.grid_configure(padx=6,pady=6,sticky='W')
