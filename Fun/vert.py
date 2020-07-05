# -*- coding: utf-8 -*-
import re
import tkinter as tk
from tkinter import messagebox as mBox
def cut_text(text,lenth):
    textArr = re.findall('.{'+str(lenth)+'}', text)
    textArr.append(text[(len(textArr)*lenth):])
    return textArr

def verticalPrint(text,counts,Widget):
    mBox.showinfo('提示', '运行中，请耐心等待\n 文件越复杂，运行时间越久哦（关了吧，没关系的）')
    text = cut_text(text,counts)
    text[-1] = text[-1].ljust(counts,' ')
    cols = len(text)
    text.reverse()
    
    rows = []
    for i in range(counts):
        row = ''
        for col in range(cols):
            row += text[col][i]
        rows.append(row)
    
    text = '\n'.join(rows)
    
    string = ''
    for char in text:
        if  not char.isdigit() and not char==' ':
            if  (char >= u'\u0041' and char<=u'\u005a') or (char >= u'\u0061' and char<=u'\u007a'):
                char += ' '
            else:
                pass
        else:
            char +=' '     
        string += char
    
    Widget.insert(tk.INSERT,string)
    mBox.showinfo('提示', '运行完毕')
    
if __name__ == '__main__':
    x=u"凡是到达了的地方，都I want to die, but I still to my life 属于昨天。哪怕那山再青，那水再秀，那风再温柔。带深的流连便成了一种羁绊，\
绊住的不仅是双脚，还有未来。可我的钱不够[笑哭]"
#    counts = 12
#    string = verticalPrint(x,counts)
#    print(string)