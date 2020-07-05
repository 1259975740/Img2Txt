# coding: utf-8
from tkinter import messagebox as mBox
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog as fd
import sys
from threading import Thread
sys.path.append('../')
from Fun.summary import summary


class Tab4():
    def __init__(self,tab,i18n):
        self._createWidget(tab,i18n)
    
    def _createTransThread(self):
        input_text = u''+str(self.inScrTxt.get(1.0,tk.END))
        lines = int(self.linesEry.get())

        run = Thread(target=summary,args=(input_text,lines,self.outScrTxt))
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
                # 文件管理栏目
        self.inOutFrm = ttk.Frame(self.zhuo)
        self.inOutFrm.grid(column=0,row=0,sticky='W')
        
        ttk.Label(self.inOutFrm,text=i18n.input_tab3).grid(column=0,row=0)
        
        self.inScrTxt = scrolledtext.ScrolledText(self.inOutFrm,height=10,width=70,wrap=tk.WORD)
        self.inScrTxt.grid(row=1,column=0,sticky='W',padx=6,pady=6)
        self.inScrTxt.insert(tk.INSERT,"各位为疫情防控而努力的仝仁们，新冠病毒传染之迅速，以致灾祸遍地，几成不可收\
拾之局。剧烈之时，疫死者上万。当此之际，吾辈当勠力同心，协救世之热忱，往而扑疫\
症也。\
拙者不才，愿效绵薄之力。今论文所提大流行之模型者，或可作预断某地区灾情状况\
之用。进而根据该地疫情之剧烈，采取相应之措施。另有无症感染者，此亦疫情之症结所\
在。其人伏病腠理，而寻常之检测难于识别矣。归而传诸人，遂使疫情火上浇油，此不可\
不察也。然则全民普测亦十分不切实际，盖倾举国之物力难为也。故本文所述之多重分\
层抽样检测方法，细可至某个地域、年龄段，洞烛无遗，或可对无症感染者之检验有所益\
助。亦可参考本文所述之抽样、而后U 检验之方法，以断定某地域是否应做全民普测，良\
省力也。\
盖斯肺瘟之由来，传播诸人，是故隔离得当则灾祸弥销。然无知之人，因疑生惧，私\
行潜逃，功亏一篑而累及他人矣。或言“群体免疫”者，此亦饮鸩止渴，殊不可取。有鉴\
于此，凡隔离措施亦应加大力度，严加防控。或可依论文之方，设隔离委员会，委隔离诸\
要事于有志之士，亦可使之渐行止息矣。\
今灾情日以酷虐，望各国勿要独抱杞忧，而当相互襄助，积思广益，各奏所长。窃闻\
某国扣押他国救援物资以为己用，此实鼠目寸光之举。于世无益，于俗亦无益，而见诟百\
世耳。诸仝仁亦应广为宣告，以作各国韦弦之佩。夫卫生之不讲，房屋之不洁，街道之不\
扫，则病疫滋生，为害万端。此亦应为不发达国家者戒。有或素畏他国干政者，上下其手，\
虚报疫情。呜呼，此忒虚有其表，诚自取灭亡之举。深望各国机要务以大局为重，勿行削\
足适履之事，俾使疫情一波未平，一波复起也。而攘除泡沫，揭露实情，此亦诸仝仁之要\
务。\
余观夫中国治疫之尽善，举中央之职能，上下同心；发举国之民心，以杜传染。比及\
疫情改观，则兼济天下，不遗余力。然某国报农蛇之心，倒泼黑言。以致良善心灰，报效\
无由，诚可叹也。当今之世，有如城外池鱼，辅车相依者甚。是故唇揭齿寒，肤损毛落，\
休戚相关。此其中之利害，望各国机要慎思之！")
        ttk.Label(self.inOutFrm,text=i18n.output_tab3).grid(column=0,row=2)
        
        self.outScrTxt = scrolledtext.ScrolledText(self.inOutFrm,height=10,width=70,wrap=tk.WORD)
        self.outScrTxt.grid(row=3,column=0,sticky='W',padx=6,pady=6)

        for child in self.inOutFrm.winfo_children():
            child.grid_configure(padx=6,pady=6,sticky='W')
        
        
        
        #转换按钮
        self.butFrm = ttk.Frame(self.zhuo)
        self.butFrm.grid(column=0,row=1,sticky='W',pady=6)
        
        ttk.Label(self.butFrm,text=i18n.numOfSen).grid(column=0,row=0)
        self.lines_defaut = tk.StringVar()
        self.lines_defaut.set(3)
        self.linesEry = ttk.Entry(self.butFrm,textvariable=self.lines_defaut)
        self.linesEry.grid(column=1,row=0)
        
        self.transBut = ttk.Button(self.butFrm,text=i18n.transBut,
                                   command=self._trans)
        self.transBut.grid(column=0,row=1)
        
        
        self.cleanBut = ttk.Button(self.butFrm,text=i18n.cleanBut,
                                   command=self._clean)
        self.cleanBut.grid(column=1,row=1)
        for child in self.butFrm.winfo_children():
            child.grid_configure(padx=6,pady=6,sticky='W')
