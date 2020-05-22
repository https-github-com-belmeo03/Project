#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 17, 2019 04:53:27 PM +07  platform: Windows NT

import sys
import cv2
import matplotlib.pyplot as plt
import array as arr
import os
# import numpy as np
# from io import BufferedReader

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import GUI_support

from tkinter import filedialog
from tkinter import messagebox

from PIL import ImageTk,Image
import PIL

import cap as cp
# import camera as cm
import fuction_image as fmate
import test_number as nb
import scan as sc


        

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    GUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    GUI_support.init(w, top, *args, **kwargs)
    return (w, top)



def mHello():
        print("Hello World")

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


    

class Toplevel1:
        # แสดงภาพ
    def capture(self):
        # fmate.Process_paper()
        self.Canvas_image()


    def Canvas_image(self):
      
        self.my_img=ImageTk.PhotoImage(Image.open("box/img1.png"))
  

        self.videopanel.configure(image=self.my_img)
       
        self.out_image()
    
    def out_image(self):
        # self.readImage=[] 
        
        self.readImage=ImageTk.PhotoImage(Image.open("temp/img0.png"))
        self.readImage1=ImageTk.PhotoImage(Image.open("temp/img1.png"))
        self.readImage2=ImageTk.PhotoImage(Image.open("temp/img2.png"))
        self.readImage3=ImageTk.PhotoImage(Image.open("temp/img3.png"))
        self.readImage4=ImageTk.PhotoImage(Image.open("temp/img4.png"))
        self.readImage5=ImageTk.PhotoImage(Image.open("temp/img5.png"))
        self.readImage6=ImageTk.PhotoImage(Image.open("temp/img6.png"))
        self.readImage7=ImageTk.PhotoImage(Image.open("temp/img7.png"))
        self.readImage8=ImageTk.PhotoImage(Image.open("temp/img8.png"))
        self.readImage9=ImageTk.PhotoImage(Image.open("temp/img9.png"))
        self.readImage10=ImageTk.PhotoImage(Image.open("temp/img10.png"))
        self.readImage11=ImageTk.PhotoImage(Image.open("temp/img11.png"))
        self.readImage12=ImageTk.PhotoImage(Image.open("temp/img12.png"))
        self.readImage13=ImageTk.PhotoImage(Image.open("temp_score/img0.png"))
        self.readImage14=ImageTk.PhotoImage(Image.open("temp_score/img1.png"))
        self.readImage15=ImageTk.PhotoImage(Image.open("temp_score/img2.png"))
        
             
       
        self.videopanel1.configure(image=self.readImage)
        self.videopanel2.configure(image=self.readImage1)
        self.videopanel3.configure(image=self.readImage2)
        self.videopanel4.configure(image=self.readImage3)
        self.videopanel5.configure(image=self.readImage4)
        self.videopanel6.configure(image=self.readImage5)
        self.videopanel7.configure(image=self.readImage6)
        self.videopanel8.configure(image=self.readImage7)
        self.videopanel9.configure(image=self.readImage8)
        self.videopanel10.configure(image=self.readImage9)
        self.videopanel11.configure(image=self.readImage10)
        self.videopanel12.configure(image=self.readImage11)
        self.videopanel13.configure(image=self.readImage12)
        self.videopanel14.configure(image=self.readImage13)
        self.videopanel15.configure(image=self.readImage14)
        self.videopanel16.configure(image=self.readImage15)

        self.Text1.delete('0', tk.END)
        self.Text1_14.delete('0', tk.END)
        self.Text1_15.delete('0', tk.END)
        self.Text1_16.delete('0', tk.END)
        self.Text1_17.delete('0', tk.END)
        self.Text1_18.delete('0', tk.END)
        self.Text1_19.delete('0', tk.END)
        self.Text1_20.delete('0', tk.END)
        self.Text1_21.delete('0', tk.END)
        self.Text1_22.delete('0', tk.END)
        self.Text1_23.delete('0', tk.END)
        self.Text1_24.delete('0', tk.END)
        self.Text1_25.delete('0', tk.END)
        self.Text1_26.delete('0', tk.END)
        self.Text1_27.delete('0', tk.END)
        self.Text1_28.delete('0', tk.END)
       


       
        # แสดงค่าตัวเลขจาการทำนาย
    def num(self):
        
       
        num_test = nb.run_example()
        
        score_test = nb.run_score()

        self.Text1.delete('0', tk.END)
        self.Text1_14.delete('0', tk.END)
        self.Text1_15.delete('0', tk.END)
        self.Text1_16.delete('0', tk.END)
        self.Text1_17.delete('0', tk.END)
        self.Text1_18.delete('0', tk.END)
        self.Text1_19.delete('0', tk.END)
        self.Text1_20.delete('0', tk.END)
        self.Text1_21.delete('0', tk.END)
        self.Text1_22.delete('0', tk.END)
        self.Text1_23.delete('0', tk.END)
        self.Text1_24.delete('0', tk.END)
        self.Text1_25.delete('0', tk.END)
        self.Text1_26.delete('0', tk.END)
        self.Text1_27.delete('0', tk.END)
        self.Text1_28.delete('0', tk.END)

        # print(num_test)
        if len(num_test) == 13:
                # self.videopanel1.configure(image=num_test[0])
 
                self.Text1.insert(tk.END,num_test[0])
                self.Text1_14.insert(tk.END,num_test[1])
                self.Text1_15.insert(tk.END,num_test[2])
                self.Text1_16.insert(tk.END,num_test[3])
                self.Text1_17.insert(tk.END,num_test[4])
                self.Text1_18.insert(tk.END,num_test[5])
                self.Text1_19.insert(tk.END,num_test[6])
                self.Text1_20.insert(tk.END,num_test[7])
                self.Text1_21.insert(tk.END,num_test[8])
                self.Text1_22.insert(tk.END,num_test[9])
                self.Text1_23.insert(tk.END,num_test[10])
                self.Text1_24.insert(tk.END,num_test[11])
                self.Text1_25.insert(tk.END,num_test[12])
        else:
                self.Text1.insert(tk.END,num_test[0])
                self.Text1_14.insert(tk.END,num_test[1])
                self.Text1_15.insert(tk.END,num_test[2])  
                self.Text1_16.insert(tk.END,num_test[3])
                self.Text1_17.insert(tk.END,num_test[4])
                self.Text1_18.insert(tk.END,num_test[5])
                self.Text1_19.insert(tk.END,num_test[6])
                self.Text1_20.insert(tk.END,num_test[7])
                self.Text1_21.insert(tk.END,num_test[8])
                self.Text1_22.insert(tk.END,num_test[9])
                self.Text1_23.insert(tk.END,num_test[10])
                self.Text1_24.insert(tk.END,num_test[11])
        
        if len(score_test) == 3:
                self.Text1_26.insert(tk.END,score_test[0])
                self.Text1_27.insert(tk.END,score_test[1])
                self.Text1_28.insert(tk.END,score_test[2])
        else:
                self.Text1_27.insert(tk.END,score_test[0])
                self.Text1_28.insert(tk.END,score_test[1])
       
    def alert_info(self,data):
        if data == 1 :
                messagebox.showinfo( "ข้อผิดพลาด", "ไม่สามารถอ่านไฟล์ได้")
        elif data == 2:
                messagebox.showinfo( "ข้อผิดพลาด", "ไฟล์รูปภาพต้องเป็น '.jpg' ")


    def alert_info2(self):
        
        messagebox.showinfo( "ข้อผิดพลาด", "ไม่สามารถอ่านไฟล์ได้")

       

        

        # เรียกใช้ไฟล์ที่ได้จากการสแกน
    def browse_file(self):
        filetypes = (("files","*.jpg"),("all files","*.*"))

        filename = filedialog.askopenfile(mode="rb",title = "Select file",filetypes = filetypes )
        
        if filename != None:
                
                extension = os.path.splitext(filename.name)[1]
                # print(extension)
                data = 1
                data2 = 2
                # try:
                if extension == ".jpg":
                        try:
                                sc.scan_function(filename.name)
                                self.capture()
                        except:
                             self.alert_info(data)   
                else:
                        self.alert_info(data2)
                

                
                
                
             
        # เปิดกล้อง        
    def cap_img(self):

        cp.frame_cap()
        self.capture()
        
        # แก้ไขตัวเลข
    def edit_number(self):
        # num_test = nb.run_example()
        array_edit =[]
        array_editScore =[]
        

        e0 = self.Text1.get()
        e1 = self.Text1_14.get()
        e2 = self.Text1_15.get()
        e3 = self.Text1_16.get()
        e4 = self.Text1_17.get()
        e5 = self.Text1_18.get()
        e6 = self.Text1_19.get()
        e7 = self.Text1_20.get()
        e8 = self.Text1_21.get()
        e9 = self.Text1_22.get()
        e10 = self.Text1_23.get()
        e11 = self.Text1_24.get()
        e12 = self.Text1_25.get()
        # print(e12)
        # for i in range(0,12,+1):
        array_edit.append(e0)
        array_edit.append(e1)
        array_edit.append(e2)
        array_edit.append(e3)
        array_edit.append(e4)
        array_edit.append(e5)
        array_edit.append(e6)
        array_edit.append(e7)
        array_edit.append(e8)
        array_edit.append(e9)
        array_edit.append(e10)
        array_edit.append(e11)
        array_edit.append(e12)
        
        s1 = self.Text1_26.get()
        s2 = self.Text1_27.get()
        s3 = self.Text1_28.get()
        
       

        array_editScore.append(s1)
        array_editScore.append(s2)
        array_editScore.append(s3)
        if array_editScore != ['','',''] and array_edit != ['', '', '', '', '', '', '', '', '', '', '', '', '']:
                # print("1")
                nb.csv_file(array_editScore,array_edit)
        # print((array_edit))
        
        
                
                
   
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("810x513+516+128")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.CButton = tk.Button(top)
        self.CButton.place(relx=0.864, rely=0.097, height=34, width=67)
        self.CButton.configure(activebackground="#ececec")
        self.CButton.configure(activeforeground="#000000")
        self.CButton.configure(background="#d9d9d9")
        self.CButton.configure(disabledforeground="#a3a3a3")
        self.CButton.configure(foreground="#000000")
        self.CButton.configure(highlightbackground="#d9d9d9")
        self.CButton.configure(highlightcolor="black")
        self.CButton.configure(pady="0")
        self.CButton.configure(text='Camera')
        self.CButton.configure(command=lambda:self.cap_img())

        # self.CapButton = tk.Button(top)
        # self.CapButton.place(relx=0.864, rely=0.195, height=34, width=77)
        # self.CapButton.configure(activebackground="#ececec")
        # self.CapButton.configure(activeforeground="#000000")
        # self.CapButton.configure(background="#d9d9d9")
        # self.CapButton.configure(disabledforeground="#a3a3a3")
        # self.CapButton.configure(foreground="#000000")
        # self.CapButton.configure(highlightbackground="#d9d9d9")
        # self.CapButton.configure(highlightcolor="black")
        # self.CapButton.configure(pady="0")
        # self.CapButton.configure(text='''Capture''')
        # self.CapButton.configure(command=lambda:cm.frame_camera())

        self.bButton = tk.Button(top)
        self.bButton.place(relx=0.864, rely=0.295, height=34, width=67)
        self.bButton.configure(activebackground="#ececec")
        self.bButton.configure(activeforeground="#000000")
        self.bButton.configure(background="#d9d9d9")
        self.bButton.configure(disabledforeground="#a3a3a3")
        self.bButton.configure(foreground="#000000")
        self.bButton.configure(highlightbackground="#d9d9d9")
        self.bButton.configure(highlightcolor="black")
        self.bButton.configure(pady="0")
        self.bButton.configure(text='''Browse''')
        self.bButton.configure(command=lambda:self.browse_file())
        


        
   


        self.videopanel = tk.Label(top)
        self.videopanel.place(relx=0.025, rely=0.019, relheight=0.341
                , relwidth=0.802)
        self.videopanel.configure(relief='groove')
        self.videopanel.configure(foreground="black")
       
      
        

        self.Labelframe2 = tk.LabelFrame(top)
        self.Labelframe2.place(relx=0.025, rely=0.39, relheight=0.263
                , relwidth=0.802)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''HCR''')
        self.Labelframe2.configure(background="#d9d9d9")

        self.Labelframe3 = tk.LabelFrame(top)
        self.Labelframe3.place(relx=0.025, rely=0.70, relheight=0.263
                , relwidth=0.802)
        self.Labelframe3.configure(relief='groove')
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''SCORE''')
        self.Labelframe3.configure(background="#d9d9d9")

        self.videopanel14 = tk.Label(self.Labelframe3)
        self.videopanel14.place(relx=0.015, rely=0.10, relheight=0.800
                , relwidth=0.100)
        self.videopanel14.configure(background="#d9d9d9")
        self.videopanel14.configure(borderwidth="2")
        self.videopanel14.configure(relief="ridge")


        self.videopanel15 = tk.Label(self.Labelframe3)
        self.videopanel15.place(relx=0.2, rely=0.10, relheight=0.800
                , relwidth=0.100)
        self.videopanel15.configure(background="#d9d9d9")
        self.videopanel15.configure(borderwidth="2")
        self.videopanel15.configure(relief="ridge")

        self.videopanel16 = tk.Label(self.Labelframe3)
        self.videopanel16.place(relx=0.385, rely=0.10, relheight=0.800
                , relwidth=0.100)
        self.videopanel16.configure(background="#d9d9d9")
        self.videopanel16.configure(borderwidth="2")
        self.videopanel16.configure(relief="ridge")

        self.Text1_26 = tk.Entry(self.Labelframe3)
        self.Text1_26.place(relx=0.120, rely=0.21, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_26.configure(background="white")
        self.Text1_26.configure(font="TkTextFont")
        self.Text1_26.configure(foreground="black")

        self.Text1_27 = tk.Entry(self.Labelframe3)
        self.Text1_27.place(relx=0.305, rely=0.21, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_27.configure(background="white")
        self.Text1_27.configure(font="TkTextFont")
        self.Text1_27.configure(foreground="black")


        self.Text1_28 = tk.Entry(self.Labelframe3)
        self.Text1_28.place(relx=0.487, rely=0.21, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_28.configure(background="white")
        self.Text1_28.configure(font="TkTextFont")
        self.Text1_28.configure(foreground="black")




        # self.entry = tk.Entry(self.Labelframe3)
        # self.entry.place(relx=0.115, rely=0.10, relheight=0.800
        #         , relwidth=0.100)
        # self.entry.configure(background="#d9d9d9")
        # self.entry.configure(borderwidth="2")
        # self.entry.configure(relief="ridge")





        self.videopanel1 = tk.Label(self.Labelframe2)
        self.videopanel1.place(relx=0.015, rely=0.148, relheight=0.333
                , relwidth=0.054)
        self.videopanel1.configure(background="#d9d9d9")
        self.videopanel1.configure(borderwidth="2")
        self.videopanel1.configure(relief="ridge")

        self.videopanel2 = tk.Label(self.Labelframe2)
        self.videopanel2.place(relx=0.077, rely=0.148, relheight=0.333
                , relwidth=0.054)
        self.videopanel2.configure(background="#d9d9d9")
        self.videopanel2.configure(borderwidth="2")
        self.videopanel2.configure(relief="ridge")

        self.videopanel3 = tk.Label(self.Labelframe2)
        self.videopanel3.place(relx=0.138, rely=0.148, relheight=0.333
                , relwidth=0.054)
        self.videopanel3.configure(background="#d9d9d9")
        self.videopanel3.configure(borderwidth="2")
        self.videopanel3.configure(relief="ridge")

        self.videopanel4 = tk.Label(self.Labelframe2)
        self.videopanel4.place(relx=0.2, rely=0.148, relheight=0.333
                , relwidth=0.054)
        self.videopanel4.configure(background="#d9d9d9")
        self.videopanel4.configure(borderwidth="2")
        self.videopanel4.configure(relief="ridge")

        self.videopanel5 = tk.Label(self.Labelframe2)
        self.videopanel5.place(relx=0.262, rely=0.148, relheight=0.333
                , relwidth=0.054)
        self.videopanel5.configure(background="#d9d9d9")
        self.videopanel5.configure(borderwidth="2")
        self.videopanel5.configure(relief="ridge")

        self.videopanel6 = tk.Label(self.Labelframe2)
        self.videopanel6.place(relx=0.323, rely=0.148, relheight=0.333
                , relwidth=0.054)
        self.videopanel6.configure(background="#d9d9d9")
        self.videopanel6.configure(borderwidth="2")
        self.videopanel6.configure(relief="ridge")

        self.videopanel7 = tk.Label(self.Labelframe2)
        self.videopanel7.place(relx=0.385, rely=0.148, relheight=0.333
                , relwidth=0.054)
        self.videopanel7.configure(background="#d9d9d9")
        self.videopanel7.configure(borderwidth="2")
        self.videopanel7.configure(relief="ridge")

        self.videopanel8 = tk.Label(self.Labelframe2)
        self.videopanel8.place(relx=0.446, rely=0.148, relheight=0.333
                , relwidth=0.054)
        self.videopanel8.configure(background="#d9d9d9")
        self.videopanel8.configure(borderwidth="2")
        self.videopanel8.configure(relief="ridge")

        self.videopanel9 = tk.Label(self.Labelframe2)
        self.videopanel9.place(relx=0.508, rely=0.148, relheight=0.333
                , relwidth=0.054)
        self.videopanel9.configure(background="#d9d9d9")
        self.videopanel9.configure(borderwidth="2")
        self.videopanel9.configure(relief="ridge")

        self.videopanel10 = tk.Label(self.Labelframe2)
        self.videopanel10.place(relx=0.569, rely=0.148, relheight=0.333
                , relwidth=0.054)
        self.videopanel10.configure(background="#d9d9d9")
        self.videopanel10.configure(borderwidth="2")
        self.videopanel10.configure(relief="ridge")

        self.videopanel11 = tk.Label(self.Labelframe2)
        self.videopanel11.place(relx=0.631, rely=0.148, relheight=0.333
                , relwidth=0.054)
        self.videopanel11.configure(background="#d9d9d9")
        self.videopanel11.configure(borderwidth="2")
        self.videopanel11.configure(relief="ridge")

        self.videopanel12 = tk.Label(self.Labelframe2)
        self.videopanel12.place(relx=0.692, rely=0.148, relheight=0.333
                , relwidth=0.054)
        self.videopanel12.configure(background="#d9d9d9")
        self.videopanel12.configure(borderwidth="2")
        self.videopanel12.configure(relief="ridge")

        self.videopanel13 = tk.Label(self.Labelframe2)
        self.videopanel13.place(relx=0.754, rely=0.148, relheight=0.333
                , relwidth=0.054)
        self.videopanel13.configure(background="#d9d9d9")
        self.videopanel13.configure(borderwidth="2")
        self.videopanel13.configure(relief="ridge")

       
     
     
    
      

        # self.Button1 = tk.Button(self.Labelframe2)
        # self.Button1.place(relx=0.877, rely=0.148, height=34, width=67
        #         , bordermode='ignore')
        # self.Button1.configure(activebackground="#ececec")
        # self.Button1.configure(activeforeground="#000000")
        # self.Button1.configure(background="#d9d9d9")
        # self.Button1.configure(disabledforeground="#a3a3a3")
        # self.Button1.configure(foreground="#000000")
        # self.Button1.configure(highlightbackground="#d9d9d9")
        # self.Button1.configure(highlightcolor="black")
        # self.Button1.configure(pady="0")
        # self.Button1.configure(text='''Train''')
        # self.Button1.configure(command=lambda:cnn.run_test_harness)

        self.Button2 = tk.Button(self.Labelframe2)
        self.Button2.place(relx=0.877, rely=0.248, height=34, width=67
                , bordermode='ignore')
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Process''')
        self.Button2.configure(command=lambda:self.num())

        self.Button3 = tk.Button(self.Labelframe2)
        self.Button3.place(relx=0.877, rely=0.548, height=34, width=67
                , bordermode='ignore')
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Confirm''')
        self.Button3.configure(command=lambda:self.edit_number())
        # print(num_test)
        # print(nb.run_example())


        self.Text1 = tk.Entry(self.Labelframe2)
        self.Text1.place(relx=0.015, rely=0.600, relheight=0.178, relwidth=0.052
                , bordermode='ignore')
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        # self.Text1.configure(highlightbackground="#d9d9d9")
        # self.Text1.configure(highlightcolor="black")
        # self.Text1.configure(insertbackground="black")
        # self.Text1.configure(selectbackground="#c4c4c4")
        # self.Text1.configure(selectforeground="black")
        # self.Text1.configure(undo="1")
        # self.Text1.configure(wrap="word")
       

        self.Text1_14 = tk.Entry(self.Labelframe2)
        self.Text1_14.place(relx=0.077, rely=0.600, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_14.configure(background="white")
        self.Text1_14.configure(font="TkTextFont")
        self.Text1_14.configure(foreground="black")
        # self.Text1_14.configure(highlightbackground="#d9d9d9")
        # self.Text1_14.configure(highlightcolor="black")
        # self.Text1_14.configure(insertbackground="black")
        # self.Text1_14.configure(selectbackground="#c4c4c4")
        # self.Text1_14.configure(selectforeground="black")
        # self.Text1_14.configure(undo="1")
        # self.Text1_14.configure(wrap="word")

        self.Text1_15 = tk.Entry(self.Labelframe2)
        self.Text1_15.place(relx=0.138, rely=0.600, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_15.configure(background="white")
        self.Text1_15.configure(font="TkTextFont")
        self.Text1_15.configure(foreground="black")
        # self.Text1_15.configure(highlightbackground="#d9d9d9")
        # self.Text1_15.configure(highlightcolor="black")
        # self.Text1_15.configure(insertbackground="black")
        # self.Text1_15.configure(selectbackground="#c4c4c4")
        # self.Text1_15.configure(selectforeground="black")
        # self.Text1_15.configure(undo="1")
        # self.Text1_15.configure(wrap="word")

        self.Text1_16 = tk.Entry(self.Labelframe2)
        self.Text1_16.place(relx=0.2, rely=0.600, relheight=0.178, relwidth=0.052
                , bordermode='ignore')
        self.Text1_16.configure(background="white")
        self.Text1_16.configure(font="TkTextFont")
        self.Text1_16.configure(foreground="black")
        # self.Text1_16.configure(highlightbackground="#d9d9d9")
        # self.Text1_16.configure(highlightcolor="black")
        # self.Text1_16.configure(insertbackground="black")
        # self.Text1_16.configure(selectbackground="#c4c4c4")
        # self.Text1_16.configure(selectforeground="black")
        # self.Text1_16.configure(undo="1")
        # self.Text1_16.configure(wrap="word")

        self.Text1_17 = tk.Entry(self.Labelframe2)
        self.Text1_17.place(relx=0.262, rely=0.600, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_17.configure(background="white")
        self.Text1_17.configure(font="TkTextFont")
        self.Text1_17.configure(foreground="black")
        # self.Text1_17.configure(highlightbackground="#d9d9d9")
        # self.Text1_17.configure(highlightcolor="black")
        # self.Text1_17.configure(insertbackground="black")
        # self.Text1_17.configure(selectbackground="#c4c4c4")
        # self.Text1_17.configure(selectforeground="black")
        # self.Text1_17.configure(undo="1")
        # self.Text1_17.configure(wrap="word")

        self.Text1_18 = tk.Entry(self.Labelframe2)
        self.Text1_18.place(relx=0.323, rely=0.600, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_18.configure(background="white")
        self.Text1_18.configure(font="TkTextFont")
        self.Text1_18.configure(foreground="black")
        # self.Text1_18.configure(highlightbackground="#d9d9d9")
        # self.Text1_18.configure(highlightcolor="black")
        # self.Text1_18.configure(insertbackground="black")
        # self.Text1_18.configure(selectbackground="#c4c4c4")
        # self.Text1_18.configure(selectforeground="black")
        # self.Text1_18.configure(undo="1")
        # self.Text1_18.configure(wrap="word")

        self.Text1_19 = tk.Entry(self.Labelframe2)
        self.Text1_19.place(relx=0.385, rely=0.600, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_19.configure(background="white")
        self.Text1_19.configure(font="TkTextFont")
        self.Text1_19.configure(foreground="black")
        # self.Text1_19.configure(highlightbackground="#d9d9d9")
        # self.Text1_19.configure(highlightcolor="black")
        # self.Text1_19.configure(insertbackground="black")
        # self.Text1_19.configure(selectbackground="#c4c4c4")
        # self.Text1_19.configure(selectforeground="black")
        # self.Text1_19.configure(undo="1")
        # self.Text1_19.configure(wrap="word")

        self.Text1_20 = tk.Entry(self.Labelframe2)
        self.Text1_20.place(relx=0.446, rely=0.600, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_20.configure(background="white")
        self.Text1_20.configure(font="TkTextFont")
        self.Text1_20.configure(foreground="black")
        # self.Text1_20.configure(highlightbackground="#d9d9d9")
        # self.Text1_20.configure(highlightcolor="black")
        # self.Text1_20.configure(insertbackground="black")
        # self.Text1_20.configure(selectbackground="#c4c4c4")
        # self.Text1_20.configure(selectforeground="black")
        # self.Text1_20.configure(undo="1")
        # self.Text1_20.configure(wrap="word")

        self.Text1_21 = tk.Entry(self.Labelframe2)
        self.Text1_21.place(relx=0.508, rely=0.600, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_21.configure(background="white")
        self.Text1_21.configure(font="TkTextFont")
        self.Text1_21.configure(foreground="black")
        # self.Text1_21.configure(highlightbackground="#d9d9d9")
        # self.Text1_21.configure(highlightcolor="black")
        # self.Text1_21.configure(insertbackground="black")
        # self.Text1_21.configure(selectbackground="#c4c4c4")
        # self.Text1_21.configure(selectforeground="black")
        # self.Text1_21.configure(undo="1")
        # self.Text1_21.configure(wrap="word")

        self.Text1_22 = tk.Entry(self.Labelframe2)
        self.Text1_22.place(relx=0.569, rely=0.600, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_22.configure(background="white")
        self.Text1_22.configure(font="TkTextFont")
        self.Text1_22.configure(foreground="black")
        # self.Text1_22.configure(highlightbackground="#d9d9d9")
        # self.Text1_22.configure(highlightcolor="black")
        # self.Text1_22.configure(insertbackground="black")
        # self.Text1_22.configure(selectbackground="#c4c4c4")
        # self.Text1_22.configure(selectforeground="black")
        # self.Text1_22.configure(undo="1")
        # self.Text1_22.configure(wrap="word")

        self.Text1_23 = tk.Entry(self.Labelframe2)
        self.Text1_23.place(relx=0.631, rely=0.600, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_23.configure(background="white")
        self.Text1_23.configure(font="TkTextFont")
        self.Text1_23.configure(foreground="black")
        # self.Text1_23.configure(highlightbackground="#d9d9d9")
        # self.Text1_23.configure(highlightcolor="black")
        # self.Text1_23.configure(insertbackground="black")
        # self.Text1_23.configure(selectbackground="#c4c4c4")
        # self.Text1_23.configure(selectforeground="black")
        # self.Text1_23.configure(undo="1")
        # self.Text1_23.configure(wrap="word")

        self.Text1_24 = tk.Entry(self.Labelframe2)
        self.Text1_24.place(relx=0.692, rely=0.600, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_24.configure(background="white")
        self.Text1_24.configure(font="TkTextFont")
        self.Text1_24.configure(foreground="black")
        # self.Text1_24.configure(highlightbackground="#d9d9d9")
        # self.Text1_24.configure(highlightcolor="black")
        # self.Text1_24.configure(insertbackground="black")
        # self.Text1_24.configure(selectbackground="#c4c4c4")
        # self.Text1_24.configure(selectforeground="black")
        # self.Text1_24.configure(undo="1")
        # self.Text1_24.configure(wrap="word")

        self.Text1_25 = tk.Entry(self.Labelframe2)
        self.Text1_25.place(relx=0.754, rely=0.600, relheight=0.178
                , relwidth=0.052, bordermode='ignore')
        self.Text1_25.configure(background="white")
        self.Text1_25.configure(font="TkTextFont")
        self.Text1_25.configure(foreground="black")
        # self.Text1_25.configure(highlightbackground="#d9d9d9")
        # self.Text1_25.configure(highlightcolor="black")
        # self.Text1_25.configure(insertbackground="black")
        # self.Text1_25.configure(selectbackground="#c4c4c4")
        # self.Text1_25.configure(selectforeground="black")
        # self.Text1_25.configure(undo="1")
        # self.Text1_25.configure(wrap="word")

  

if __name__ == '__main__':
    vp_start_gui()

    



