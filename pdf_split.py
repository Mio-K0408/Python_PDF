# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:02:02 2020

@author: Mio
"""

import os,glob

from PyPDF2 import PdfFileWriter,PdfFileReader

start_pages = [1,4,63,121,152,164,184,198,207,221,246,259,309,317]      #開始ページ
end_pages = [3,62,120,151,163,183,197,206,220,245,258,308,316,330]      #終了ページ
names = ["導入","Javaの特徴","基本構文","クラスの連携","オブジェクト指向とは",\
         "継承","インターフェース","カプセル化","ポリモルフィズム","例外処理",\
         "Javadocの読み方","APIの活用","デバッガの使い方","そのほかの文法"] #各章のタイトル


for file_name in glob.glob(r'C:\Users\Mio\Desktop\split_prac\JavaProgramming.pdf'):    #ファイル名の取得
    (name,extention) = os.path.splitext(file_name)  #ファイル名と拡張子を個別に取得
    pdf_file_reader = PdfFileReader(file_name)  #ファイルの中身を取得
    #page_nums = pdf_file_reader.getNumPages()   #PDFのページ数を取得

"""    
for num in range(page_nums): #ページを指定   
    file_object  = pdf_file_reader.getPage(num)#そのページのPDFの内容を取得
    pdf_file_name = name + '_' +str(num+1) + '.pdf' #分割後のファイル名のルール決め
    pdf_file_writer = PdfFileWriter()   #インスタンス化
    with open(pdf_file_name,'wb') as f: #ファイルオープン、ファイル名は19行目の
        pdf_file_writer.addPage(file_object)    #addPageで18行目で取り出したPDFの中身を追加
        pdf_file_writer.write(f)    #openしたファイルに22行目で追加したPDFの中身を書き込み
"""
for name,start_page,end_page in zip(names,start_pages,end_pages):       #最初に作成したリストでループ
    pdf_file_writer = PdfFileWriter()
    pdf_file_name = name + '.pdf'
    with open(pdf_file_name,'wb') as f:
        for num in range(start_page-1,end_page):      #開始インデックスは0スタートだからページ数-1
            pdf_file_writer.addPage(pdf_file_reader.getPage(num))       #PDFを取得し、追加
            pdf_file_writer.write(f)
    
