# coding: utf-8
from tkinter import messagebox as mBox
import tkinter as tk
from tkinter import ttk
from sys import exit
from tkinter import scrolledtext
from tkinter import Menu
from Tab2 import *
from Tab3 import *
from Tab4 import *
from I18N import *
import sys
import os
from os import path
sys.path.append('../')
from Fun import screenShot
from tkinter import filedialog as fd
from Fun import img2text
from threading import Thread

class OOP:
    def __init__(self):
        self.win = tk.Tk()
        self.win.resizable(0,0)    #这个是设置窗口不可缩放
        self.i18n = I18N('chi')
        self._createWidget()
        self.win.mainloop()
        
    def _quit(self):    #设置一个 menu 菜单项的激活函数
        self.win.quit()    #退出
        self.win.destroy()   #销毁
        exit()   #结束程序
    def _chi(self):
        self.win.quit()
        self.win.destroy()
        self.win = tk.Tk()
        self.win.resizable(0,0)    #这个是设置窗口不可缩放
        self.i18n = I18N('chi')
        self._createWidget()
        self.win.mainloop()
        
    def _jap(self):
        self.win.quit()
        self.win.destroy()
        self.win = tk.Tk()
        self.win.resizable(0,0)    #这个是设置窗口不可缩放
        self.i18n = I18N('jap')
        self._createWidget()
        self.win.mainloop()
        
    def _eng(self):
        self.win.quit()
        self.win.destroy()
        self.win = tk.Tk()
        self.win.resizable(0,0)    #这个是设置窗口不可缩放
        self.i18n = I18N('eng')
        self._createWidget()
        self.win.mainloop()
        
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
         
    def _getEngineFile(self):
        fDir = os.path.join(r'C:\Program Files\Tesseract-OCR')
        fName = fd.askopenfilename(parent=self.inOutFrm,initialdir=fDir)
        fPath = path.dirname(fName)
        self.engEry.delete(0,tk.END)   
        self.engEry.insert(0,fName)   
        
    def _screenShot(self):
        iptFileName = screenShot.buttonCaptureClick(self.win)
        self.win.state('normal')
        self.inEry.delete(0,tk.END)   
        self.inEry.insert(0,iptFileName)  
    
    
    def _createTransThread(self):
        flag = self.radVar.get()
        run = Thread(target=img2text.img2text,args=(self.engEry.get(),self.inEry.get(),
                                              self.outEry.get(),self.scrTxt,self.radVar.get()))
        
        
        run.setDaemon(True)
        run.start()
        
    def _clean(self):
        if mBox.askyesno("百变小T", 
                               "确定清空文本预览里的内容吗？"):
        
            self.scrTxt.delete(1.0,tk.END)
    
    def _trans(self):
        self._createTransThread()
        
    def _flag(self):
        pass
    
    def _createWidget(self):
        self.menuBar = Menu(self.win)
        self.win.configure(menu=self.menuBar)
        self.win.title(self.i18n.title)
        self.win.iconbitmap(r'../app.ico')
        self.startMenu = Menu(self.menuBar,tearoff=0)
        # pop menus：
        self.I18NMenu = Menu(self.startMenu,tearoff=0)    # 这个是 Menu 中的 Menu 了，可以一直这样嵌套下去
        self.I18NMenu.add_command(label=self.i18n.labChi,command=self._chi)
        self.I18NMenu.add_command(label=self.i18n.labJap,command=self._jap)
        self.I18NMenu.add_command(label=self.i18n.labEng,command=self._eng)
        self.startMenu.add_cascade(label=self.i18n.labTrans,menu=self.I18NMenu)
        
        
        self.startMenu.add_command(label=self.i18n.labQuit,command=self._quit)
        self.menuBar.add_cascade(label=self.i18n.labStart,menu=self.startMenu)
        
        self.tabControl = ttk.Notebook(self.win)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1,text=self.i18n.labTab1)
        self.tabControl.add(self.tab2,text=self.i18n.labTab2)
        self.tabControl.add(self.tab3,text=self.i18n.labTab3)
        self.tabControl.add(self.tab4,text=self.i18n.labTab4)
        self.tabControl.pack(fill='both',expand=1)
        
        self.zhuo = ttk.Frame(self.tab1)
        self.zhuo.grid(column=0,row=0)
        
        # 文件管理栏目
        
        
        self.inOutFrm = ttk.Frame(self.zhuo)
        self.inOutFrm.grid(column=0,row=0,sticky='W')
        self.fDir = os.path.abspath(os.path.join( os.path.dirname(__file__),".."))
        # 引擎
        self.engine = ttk.Button(self.inOutFrm,text=self.i18n.engine,
                            command=self._getEngineFile)
        self.engine.grid(row=2,column=0)
        self.eng_value = tk.StringVar()
        self.eng_value.set(r'C:\Program Files\Tesseract-OCR\tesseract.exe')
        
        self.engEry = ttk.Entry(self.inOutFrm,width=60,textvariable=self.eng_value)
        self.engEry.grid(row=2,column=1)
        
        self.inBut = ttk.Button(self.inOutFrm,text=self.i18n.inBut,
                            command=self._getIptFileName)
        self.inBut.grid(column=0,row=0)
        self.inBut_value = tk.StringVar()
        self.inBut_value.set(self.fDir+r'\Input')
        self.inEry = ttk.Entry(self.inOutFrm,width=60,textvariable=self.inBut_value)
        self.inEry.grid(column=1,row=0)
        
        
        
        self.outBut = ttk.Button(self.inOutFrm,text=self.i18n.outBut,
                                 command=self._getOptFileName)
        self.outBut.grid(column=0,row=1)
        self.outBut_value = tk.StringVar()
        self.outBut_value.set(self.fDir+r'\Output')
        self.outEry = ttk.Entry(self.inOutFrm,width=60,textvariable=self.outBut_value)
        self.outEry.grid(column=1,row=1)
        
        for child in self.inOutFrm.winfo_children():
            child.grid_configure(padx=6,pady=6,sticky='W')
        
        #语言选项
                #语言选项
        self.langFrm = ttk.Frame(self.zhuo)
        self.langFrm.grid(column=0,row=1,sticky='W',pady=6)
                
        LANG = [self.i18n.lang_chi,self.i18n.lang_eng,self.i18n.lang_jap,self.i18n.lang_tra,self.i18n.lang_math]    #设置颜色
        VALUE = ['chi_sim','eng','jpn','chi_tra','equ']
        
        self.radVar = tk.StringVar()    #声明
        self.radVar.set('chi_sim')    #初始化值，如果不初始化，这某个圆框会被 默认 选中
        
        ttk.Label(self.langFrm,text=self.i18n.label_tab).grid(column=0,row=0)        
        for col in range(5):
            rad = 'Rad'+ str(col)    #这个用于设置 对象名
            self.rad = tk.Radiobutton(self.langFrm,variable=self.radVar,value=VALUE[col],text=LANG[col])
            #实例化一个圆框对象，设置变量为 radVar。被选中时，其值设置为 col。 设置 圆框后面的字符为 COLOR
            # 设置触发事件为 clickRadio 函数
            self.rad.grid(column=col+1,row=0,sticky=tk.W)    #设置位置，且左对齐
            
        for child in self.langFrm.winfo_children():
            child.grid_configure(padx=6,pady=6,sticky='W')
        
        
        
        #截图与转换按钮
        self.butFrm = ttk.Frame(self.zhuo)
        self.butFrm.grid(column=0,row=2,sticky='W',pady=6)
        self.printScrBut = ttk.Button(self.butFrm,text=self.i18n.printScrBut,
                                   command=self._screenShot)
        self.printScrBut.grid(column=0,row=0)
        self.transBut = ttk.Button(self.butFrm,text=self.i18n.transBut,
                                   command=self._trans)
        self.transBut.grid(column=1,row=0)
#        self.iptBut = ttk.Button(self.butFrm,text=self.i18n.iptBut,
#                                   command=self._flag)
#        self.iptBut.grid(column=2,row=0)
        self.cleanBut = ttk.Button(self.butFrm,text=self.i18n.cleanBut,
                                   command=self._clean)
        self.cleanBut.grid(column=2,row=0)
        
        
        for child in self.butFrm.winfo_children():
            child.grid_configure(padx=6,pady=6,sticky='W')
        
        
        #滑动文字展示栏
        self.printOptFrm = ttk.LabelFrame(self.zhuo,text=self.i18n.printOptFrm)
        self.printOptFrm.grid(row=3,column=0,sticky='W')
        self.scrTxt = scrolledtext.ScrolledText(self.printOptFrm,height=20,width=70,wrap=tk.WORD)
        self.scrTxt.grid(row=0,column=0,sticky='W',padx=6,pady=6)
        
        self.tab2Widget = Tab2(self.tab2,self.i18n)
        self.tab3Widget = Tab3(self.tab3,self.i18n)
        self.tab4Widget = Tab4(self.tab4,self.i18n)
        
oop = OOP()
       
  