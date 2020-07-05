# coding: utf-8
import tkinter as tk
from tkinter import ttk
import sys
from PIL.FontFile import WIDTH
sys.path.append('../')
from Fun.vert import verticalPrint
from tkinter import messagebox as mBox
from tkinter import scrolledtext
from threading import Thread


class Tab3():
    def __init__(self,tab,i18n):
        self._createWidget(tab,i18n)

    def _createTransThread(self):
        
        input_text = u''+str(self.inScrTxt.get(1.0,tk.END))
        print(input_text)
        width = int(self.widthEry.get())
        run = Thread(target=verticalPrint,args=(input_text,width,self.outScrTxt))
        run.setDaemon(True)
        run.start()
    
    def _trans(self):
        self._createTransThread()


    def _clean(self):
        if mBox.askyesno("百变小T", 
                               "确定清空输出框里的内容吗？"):
        
            self.inScrTxt.delete(1.0,tk.END)
            self.outScrTxt.delete(1.0,tk.END)
    
       
    def _createWidget(self,tab,i18n):
        self.zhuo = ttk.Frame(tab)
        self.zhuo.grid(row=0,column=0)
        
        self.widthFrm = ttk.Frame(self.zhuo)
        self.widthFrm.grid(column=0,row=0,sticky='W',pady=6)
        ttk.Label(self.widthFrm,text=i18n.width).grid(column=0,row=0)
        self._width_default = tk.StringVar()
        self._width_default.set(6)
        self.widthEry = ttk.Entry(self.widthFrm,textvariable=self._width_default)
        self.widthEry.grid(column=1,row=0)
        

        #转换按钮
        self.butFrm = ttk.Frame(self.zhuo)
        self.butFrm.grid(column=0,row=2,sticky='W',pady=6)

        self.transBut = ttk.Button(self.butFrm,text=i18n.transBut,
                                   command=self._trans)
        self.transBut.grid(column=1,row=0)
        
        self.cleanBut = ttk.Button(self.butFrm,text=i18n.cleanBut,
                                   command=self._clean)
        self.cleanBut.grid(column=2,row=0)
        
        
        
        for child in self.butFrm.winfo_children():
            child.grid_configure(padx=6,pady=6,sticky='W')
            
        #滑动文字展示栏
        self.printOptFrm = ttk.Frame(self.zhuo)
        self.printOptFrm.grid(row=1,column=0,sticky='W')
        
        ttk.Label(self.printOptFrm,text=i18n.input_tab3).grid(column=0,row=0)
        
        self.inScrTxt = scrolledtext.ScrolledText(self.printOptFrm,height=10,width=70,wrap=tk.WORD)
        self.inScrTxt.grid(row=1,column=0,sticky='W',padx=6,pady=6)
        self.inScrTxt.insert(tk.INSERT,"凡是到达了的地方，都I want to die， but I still to my life 属于昨天。哪怕那山再青，那水再秀，那风再温柔。带深的流连便成了一种羁绊，\
绊住的不仅是双脚，还有未来。可我的钱不够笑哭")
        ttk.Label(self.printOptFrm,text=i18n.output_tab3).grid(column=0,row=2)
        
        self.outScrTxt = scrolledtext.ScrolledText(self.printOptFrm,height=10,width=70,wrap=tk.WORD)
        self.outScrTxt.grid(row=3,column=0,sticky='W',padx=6,pady=6)
        
        for child in self.printOptFrm.winfo_children():
            child.grid_configure(padx=6,pady=6,sticky='W')