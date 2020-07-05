# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:52:32 2020

@author: 
"""
from pyhanlp import *
from tkinter import messagebox as mBox

import tkinter as tk

def summary(text,num,Widget):
    
    text_list = HanLP.extractSummary(text,num)
    text = '\n'.join([t for t in text_list])
    Widget.insert(tk.INSERT,text)
    mBox.showinfo('提示', '运行完毕')
    

if __name__ == "__main__":
    summary_list = summary('“芦花滩上有扁舟， 俊杰黄昏独自游， 义到尽头原是命， 反躬逃难必无忧。”\
这是一首出自《水浒传》中吴用留下的藏头反诗；电视剧《裂变》中汉奸“蝙蝠”也曾\
使用数字对应书本页面和文字的方法传递消息给日寇；电影《暗算》中更是提到了黄依\
依解决多种密文的具体情节；甚至连动画片《名侦探柯南》也出现了 skytale 加密的细\
节。事实上，密文不仅存在于荧幕中，而且深入到生活的方方面面，例如用于存储互联\
网消息的 cookie、以及互联网安全中常提到的数字签名、在银行等网站上填写个人信息\
时，都会用一定的手段将明文加密成密文传输到在远处的服务器中，可以说，在互联网\
的世界里，只要有比特流动，就一定会有加密的存在。为此，各大高校还设立了专门的\
学科，如密码学、密码分析学、密码史等。不得不说，密码的发展更数学密切相关、大\
多数的密码学家都兼任数学家的身份，而密码学，这一学科在战争时代更是快速地发展。\
以下将会介绍密码学的发展史、以及一些经典密码学的典型加密方法和其对应的解密方\
法的介绍、文章最后会简单地提及现代密码学的一些实现手段',5)
    print(summary_list)
    