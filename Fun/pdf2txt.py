# coding: utf-8
import argparse
import logging
import sys
import pdfminer3.settings
pdfminer3.settings.STRICT = False
import pdfminer3.high_level
import pdfminer3.layout
from pdfminer3.image import ImageWriter
import tkinter as tk
from tkinter import messagebox as mBox


def extract_text(files=[], outfile='-',
            _py2_no_more_posargs=None,  
            no_laparams=False, all_texts=None, detect_vertical=None, # LAParams
            word_margin=None, char_margin=None, line_margin=None, boxes_flow=None, # LAParams
            output_type='text', codec='utf-8', strip_control=False,
            maxpages=0, page_numbers=None, password="", scale=1.0, rotation=0,
            layoutmode='normal', output_dir=None, debug=False,
            disable_caching=False, **other):
    if _py2_no_more_posargs is not None:
        raise ValueError("Too many positional arguments passed.")
    if not files:
        raise ValueError("Must provide files to work upon!")

    if not no_laparams:
        laparams = pdfminer3.layout.LAParams()
        for param in ("all_texts", "detect_vertical", "word_margin", "char_margin", "line_margin", "boxes_flow"):
            paramv = locals().get(param, None)
            if paramv is not None:
                setattr(laparams, param, paramv)
    else:
        laparams = None

    imagewriter = None
    if output_dir:
        imagewriter = ImageWriter(output_dir)

    if output_type == "text" and outfile != "-":
        for override, alttype in (  (".htm", "html"),
                                    (".html", "html"),
                                    (".xml", "xml"),
                                    (".tag", "tag") ):
            if outfile.endswith(override):
                output_type = alttype

    if outfile == "-":
        outfp = sys.stdout
        if outfp.encoding is not None:
            codec = 'utf-8'
    else:
        outfp = open(outfile, "wb")


    for fname in files:
        with open(fname, "rb") as fp:
            pdfminer3.high_level.extract_text_to_fp(fp, **locals())
    return outfp



def trans(files, outfile):
    mBox.showinfo('提示', '运行中，请耐心等待\n 文件越复杂，运行时间越久哦（关了吧，没关系的）')
    outfp = extract_text(files=files,outfile=outfile)
    outfp.close()
    mBox.showinfo('提示ʾ', '运行完毕')


if __name__ == '__main__': 
    trans(files=['E:/java-2020-03/eclipse/workspace/Img2Txt/Fun/test.pdf'],outfile='output.html')
