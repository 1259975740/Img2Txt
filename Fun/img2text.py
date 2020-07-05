# coding: utf-8
import pytesseract
from PIL import Image
from tkinter import messagebox as mBox
import tkinter as tk
import os

def img2text(engine_path,img_path,text_path,Widget,lang):
    pytesseract.pytesseract.tesseract_cmd = engine_path
    mBox.showinfo('提示', '运行中，请耐心等待\n 文件越复杂，运行时间越久哦（关了吧，没关系的）')
    text = pytesseract.image_to_string(Image.open(img_path),lang=lang)

    with open(text_path+r'\output.txt', "w", encoding='utf-8') as f:
        f.write(text)
        f.close()
    mBox.showinfo('提示', '运行完毕')
    Widget.insert(tk.INSERT,text)
 
def img2text_TEST(engine_path,img_path,text_path):
    pytesseract.pytesseract.tesseract_cmd = engine_path  
    text = pytesseract.image_to_string(Image.open(img_path),lang='chi_sim')

    with open(text_path+r'\output.txt', "w", encoding='utf-8') as f:
        f.write(text)
        f.close()
    mBox.showinfo('提示', '运行完毕')

if __name__ == '__main__':    
    engine_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img_path = r'E:\java-2020-03\eclipse\workspace\Img2Txt\Input\test_math.jpg'
    text_path = r'E:\java-2020-03\eclipse\workspace\Img2Txt\Output'
    img2text_TEST(engine_path,img_path,text_path) 

 
