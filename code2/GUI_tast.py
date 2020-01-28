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
import sys
from PIL import ImageTk,Image
import PIL
import cv2

class Graphical_user_interface():

    def setGui(self):
        '''Starting point when module is the main routine.'''
        global root
        root = tk.Tk()
        frame(root)
        root.mainloop()

class frame():

    def eventCapButton(self):
        print("eventCapButton")
        # self.videopanel.pack()
        self.capImg = ImageTk.PhotoImage(Image.open("box/img1.png"))
        self.videopanel.configure(image=self.capImg)


    def loadVideo(self):
        print("loadVideo")
        # self.Canvasframe1 = tk.Canvas(self.Top)


    # def loadVideo(self):
    #
    #     self.vid = cv2.VideoCapture(0)
    #     if not self.vid.isOpened():
    #         raise ValueError("Unable to open video source", 0)
    #
    #     self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    #     self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    #
    #     self.panel.pack_forget()
    #     self.video_source = 0
    #
    #     self.delay = 15
    #     self.update()
    #
    # def get_frame(self):
    #     if self.vid.isOpened():
    #         ret, frame = self.vid.read()
    #         if ret:
    #             return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    #         else:
    #             return (ret, None)
    #
    #
    # def update(self):
    #     ret, frame = self.get_frame()
    #     if ret:
    #         self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    #         self.Canvasframe1.create_image(0, 0, image=self.photo, anchor=tk.NW)
    #         self.Top.after(self.delay, self.update)





    def __init__(self, top=None):
        self.Top = top

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("810x513+516+128")
        top.minsize(120, 1)
        top.maxsize(3844, 1061)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.CButton = tk.Button(top,command=self.loadVideo)
        self.CButton = tk.Button(top)
        self.CButton.place(relx=0.864, rely=0.097, height=34, width=77)
        self.CButton.configure(activebackground="#ececec")
        self.CButton.configure(activeforeground="#000000")
        self.CButton.configure(background="#d9d9d9")
        self.CButton.configure(disabledforeground="#a3a3a3")
        self.CButton.configure(foreground="#000000")
        self.CButton.configure(highlightbackground="#d9d9d9")
        self.CButton.configure(highlightcolor="black")
        self.CButton.configure(pady="0")
        self.CButton.configure(text='Camera')
        # self.CButton.configure(command=lambda:cp.frame_cap())

        self.CapButton = tk.Button(top,command=self.eventCapButton)
        self.CapButton.place(relx=0.864, rely=0.195, height=34, width=77)
        self.CapButton.configure(activebackground="#ececec")
        self.CapButton.configure(activeforeground="#000000")
        self.CapButton.configure(background="#d9d9d9")
        self.CapButton.configure(disabledforeground="#a3a3a3")
        self.CapButton.configure(foreground="#000000")
        self.CapButton.configure(highlightbackground="#d9d9d9")
        self.CapButton.configure(highlightcolor="black")
        self.CapButton.configure(pady="0")
        self.CapButton.configure(text='''Capture''')

        self.videopanel = tk.Label(top)
        self.videopanel.place(relx=0.025, rely=0.019, relheight=0.55, relwidth=0.802)


        # self.Canvasframe1.place(relx=0.025, rely=0.019, relheight=0.9, relwidth=0.802)

        # self.Canvasframe1.place(relx=0.025, rely=0.019, relheight=0.341, relwidth=0.802)
        # self.Canvasframe1.configure(relief='groove')
        # self.Canvasframe1.configure(background="#d9d9d9")



        # #
        # self.Labelframe2 = tk.LabelFrame(top)
        # self.Labelframe2.place(relx=0.025, rely=0.39, relheight=0.263
        #                        , relwidth=0.802)
        # self.Labelframe2.configure(relief='groove')
        # self.Labelframe2.configure(foreground="black")
        # self.Labelframe2.configure(text='''HCR''')
        # self.Labelframe2.configure(background="#d9d9d9")
        #
        # self.TFrame1 = ttk.Frame(self.Labelframe2)
        # self.TFrame1.place(relx=0.015, rely=0.148, relheight=0.333
        #                    , relwidth=0.054, bordermode='ignore')
        # self.TFrame1.configure(relief='groove')
        # self.TFrame1.configure(borderwidth="2")
        # self.TFrame1.configure(relief="groove")
        #
        # self.TFrame1_1 = ttk.Frame(self.Labelframe2)
        # self.TFrame1_1.place(relx=0.077, rely=0.148, relheight=0.333
        #                      , relwidth=0.054, bordermode='ignore')
        # self.TFrame1_1.configure(relief='groove')
        # self.TFrame1_1.configure(borderwidth="2")
        # self.TFrame1_1.configure(relief="groove")
        #
        # self.TFrame1_2 = ttk.Frame(self.Labelframe2)
        # self.TFrame1_2.place(relx=0.138, rely=0.148, relheight=0.333
        #                      , relwidth=0.054, bordermode='ignore')
        # self.TFrame1_2.configure(relief='groove')
        # self.TFrame1_2.configure(borderwidth="2")
        # self.TFrame1_2.configure(relief="groove")
        #
        # self.TFrame1_3 = ttk.Frame(self.Labelframe2)
        # self.TFrame1_3.place(relx=0.2, rely=0.148, relheight=0.333
        #                      , relwidth=0.054, bordermode='ignore')
        # self.TFrame1_3.configure(relief='groove')
        # self.TFrame1_3.configure(borderwidth="2")
        # self.TFrame1_3.configure(relief="groove")
        #
        # self.TFrame1_4 = ttk.Frame(self.Labelframe2)
        # self.TFrame1_4.place(relx=0.262, rely=0.148, relheight=0.333
        #                      , relwidth=0.054, bordermode='ignore')
        # self.TFrame1_4.configure(relief='groove')
        # self.TFrame1_4.configure(borderwidth="2")
        # self.TFrame1_4.configure(relief="groove")
        #
        # self.TFrame1_5 = ttk.Frame(self.Labelframe2)
        # self.TFrame1_5.place(relx=0.323, rely=0.148, relheight=0.333
        #                      , relwidth=0.054, bordermode='ignore')
        # self.TFrame1_5.configure(relief='groove')
        # self.TFrame1_5.configure(borderwidth="2")
        # self.TFrame1_5.configure(relief="groove")
        #
        # self.TFrame1_6 = ttk.Frame(self.Labelframe2)
        # self.TFrame1_6.place(relx=0.385, rely=0.148, relheight=0.333
        #                      , relwidth=0.054, bordermode='ignore')
        # self.TFrame1_6.configure(relief='groove')
        # self.TFrame1_6.configure(borderwidth="2")
        # self.TFrame1_6.configure(relief="groove")

        # self.TFrame1_7 = ttk.Frame(self.Labelframe2)
        # self.TFrame1_7.place(relx=0.446, rely=0.148, relheight=0.333
        #                      , relwidth=0.054, bordermode='ignore')
        # self.TFrame1_7.configure(relief='groove')
        # self.TFrame1_7.configure(borderwidth="2")
        # self.TFrame1_7.configure(relief="groove")
        #
        # self.TFrame1_8 = ttk.Frame(self.TFrame1_7)
        # self.TFrame1_8.place(relx=8.857, rely=1.111, relheight=1.0, relwidth=1.0)
        #
        # self.TFrame1_8.configure(relief='groove')
        # self.TFrame1_8.configure(borderwidth="2")
        # self.TFrame1_8.configure(relief="groove")
        #
        # self.TFrame1_9 = ttk.Frame(self.Labelframe2)
        # self.TFrame1_9.place(relx=0.508, rely=0.148, relheight=0.333
        #                      , relwidth=0.054, bordermode='ignore')
        # self.TFrame1_9.configure(relief='groove')
        # self.TFrame1_9.configure(borderwidth="2")
        # self.TFrame1_9.configure(relief="groove")
        #
        # self.TFrame1_10 = ttk.Frame(self.Labelframe2)
        # self.TFrame1_10.place(relx=0.569, rely=0.148, relheight=0.333
        #                       , relwidth=0.054, bordermode='ignore')
        # self.TFrame1_10.configure(relief='groove')
        # self.TFrame1_10.configure(borderwidth="2")
        # self.TFrame1_10.configure(relief="groove")
        #
        # self.TFrame1_11 = ttk.Frame(self.Labelframe2)
        # self.TFrame1_11.place(relx=0.631, rely=0.148, relheight=0.333
        #                       , relwidth=0.054, bordermode='ignore')
        # self.TFrame1_11.configure(relief='groove')
        # self.TFrame1_11.configure(borderwidth="2")
        # self.TFrame1_11.configure(relief="groove")
        #
        # self.TFrame1_12 = ttk.Frame(self.Labelframe2)
        # self.TFrame1_12.place(relx=0.692, rely=0.148, relheight=0.333
        #                       , relwidth=0.054, bordermode='ignore')
        # self.TFrame1_12.configure(relief='groove')
        # self.TFrame1_12.configure(borderwidth="2")
        # self.TFrame1_12.configure(relief="groove")
        #
        # self.TFrame1_13 = ttk.Frame(self.Labelframe2)
        # self.TFrame1_13.place(relx=0.754, rely=0.148, relheight=0.333
        #                       , relwidth=0.054, bordermode='ignore')
        # self.TFrame1_13.configure(relief='groove')
        # self.TFrame1_13.configure(borderwidth="2")
        # self.TFrame1_13.configure(relief="groove")
        #
        # self.Button1 = tk.Button(self.Labelframe2)
        # self.Button1.place(relx=0.877, rely=0.148, height=34, width=67
        #                    , bordermode='ignore')
        # self.Button1.configure(activebackground="#ececec")
        # self.Button1.configure(activeforeground="#000000")
        # self.Button1.configure(background="#d9d9d9")
        # self.Button1.configure(disabledforeground="#a3a3a3")
        # self.Button1.configure(foreground="#000000")
        # self.Button1.configure(highlightbackground="#d9d9d9")
        # self.Button1.configure(highlightcolor="black")
        # self.Button1.configure(pady="0")
        # self.Button1.configure(text='''Train''')
        # # self.Button1.configure(command=lambda:cnn.run_test_harness() )
        #
        # self.Button2 = tk.Button(self.Labelframe2)
        # self.Button2.place(relx=0.877, rely=0.519, height=34, width=67
        #                    , bordermode='ignore')
        # self.Button2.configure(activebackground="#ececec")
        # self.Button2.configure(activeforeground="#000000")
        # self.Button2.configure(background="#d9d9d9")
        # self.Button2.configure(disabledforeground="#a3a3a3")
        # self.Button2.configure(foreground="#000000")
        # self.Button2.configure(highlightbackground="#d9d9d9")
        # self.Button2.configure(highlightcolor="black")
        # self.Button2.configure(pady="0")
        # self.Button2.configure(text='''Process''')
        #
        # self.Text1 = tk.Text(self.Labelframe2)
        # self.Text1.place(relx=0.015, rely=0.519, relheight=0.178, relwidth=0.052
        #                  , bordermode='ignore')
        # self.Text1.configure(background="white")
        # self.Text1.configure(font="TkTextFont")
        # self.Text1.configure(foreground="black")
        # self.Text1.configure(highlightbackground="#d9d9d9")
        # self.Text1.configure(highlightcolor="black")
        # self.Text1.configure(insertbackground="black")
        # self.Text1.configure(selectbackground="#c4c4c4")
        # self.Text1.configure(selectforeground="black")
        # self.Text1.configure(undo="1")
        # self.Text1.configure(wrap="word")
        #
        # self.Text1_14 = tk.Text(self.Labelframe2)
        # self.Text1_14.place(relx=0.077, rely=0.519, relheight=0.178
        #                     , relwidth=0.052, bordermode='ignore')
        # self.Text1_14.configure(background="white")
        # self.Text1_14.configure(font="TkTextFont")
        # self.Text1_14.configure(foreground="black")
        # self.Text1_14.configure(highlightbackground="#d9d9d9")
        # self.Text1_14.configure(highlightcolor="black")
        # self.Text1_14.configure(insertbackground="black")
        # self.Text1_14.configure(selectbackground="#c4c4c4")
        # self.Text1_14.configure(selectforeground="black")
        # self.Text1_14.configure(undo="1")
        # self.Text1_14.configure(wrap="word")

        # self.Text1_15 = tk.Text(self.Labelframe2)
        # self.Text1_15.place(relx=0.138, rely=0.519, relheight=0.178
        #                     , relwidth=0.052, bordermode='ignore')
        # self.Text1_15.configure(background="white")
        # self.Text1_15.configure(font="TkTextFont")
        # self.Text1_15.configure(foreground="black")
        # self.Text1_15.configure(highlightbackground="#d9d9d9")
        # self.Text1_15.configure(highlightcolor="black")
        # self.Text1_15.configure(insertbackground="black")
        # self.Text1_15.configure(selectbackground="#c4c4c4")
        # self.Text1_15.configure(selectforeground="black")
        # self.Text1_15.configure(undo="1")
        # self.Text1_15.configure(wrap="word")
        #
        # self.Text1_16 = tk.Text(self.Labelframe2)
        # self.Text1_16.place(relx=0.2, rely=0.519, relheight=0.178, relwidth=0.052
        #                     , bordermode='ignore')
        # self.Text1_16.configure(background="white")
        # self.Text1_16.configure(font="TkTextFont")
        # self.Text1_16.configure(foreground="black")
        # self.Text1_16.configure(highlightbackground="#d9d9d9")
        # self.Text1_16.configure(highlightcolor="black")
        # self.Text1_16.configure(insertbackground="black")
        # self.Text1_16.configure(selectbackground="#c4c4c4")
        # self.Text1_16.configure(selectforeground="black")
        # self.Text1_16.configure(undo="1")
        # self.Text1_16.configure(wrap="word")
        #
        # self.Text1_17 = tk.Text(self.Labelframe2)
        # self.Text1_17.place(relx=0.262, rely=0.519, relheight=0.178
        #                     , relwidth=0.052, bordermode='ignore')
        # self.Text1_17.configure(background="white")
        # self.Text1_17.configure(font="TkTextFont")
        # self.Text1_17.configure(foreground="black")
        # self.Text1_17.configure(highlightbackground="#d9d9d9")
        # self.Text1_17.configure(highlightcolor="black")
        # self.Text1_17.configure(insertbackground="black")
        # self.Text1_17.configure(selectbackground="#c4c4c4")
        # self.Text1_17.configure(selectforeground="black")
        # self.Text1_17.configure(undo="1")
        # self.Text1_17.configure(wrap="word")
        #
        # self.Text1_18 = tk.Text(self.Labelframe2)
        # self.Text1_18.place(relx=0.323, rely=0.519, relheight=0.178
        #                     , relwidth=0.052, bordermode='ignore')
        # self.Text1_18.configure(background="white")
        # self.Text1_18.configure(font="TkTextFont")
        # self.Text1_18.configure(foreground="black")
        # self.Text1_18.configure(highlightbackground="#d9d9d9")
        # self.Text1_18.configure(highlightcolor="black")
        # self.Text1_18.configure(insertbackground="black")
        # self.Text1_18.configure(selectbackground="#c4c4c4")
        # self.Text1_18.configure(selectforeground="black")
        # self.Text1_18.configure(undo="1")
        # self.Text1_18.configure(wrap="word")

        # self.Text1_19 = tk.Text(self.Labelframe2)
        # self.Text1_19.place(relx=0.385, rely=0.519, relheight=0.178
        #                     , relwidth=0.052, bordermode='ignore')
        # self.Text1_19.configure(background="white")
        # self.Text1_19.configure(font="TkTextFont")
        # self.Text1_19.configure(foreground="black")
        # self.Text1_19.configure(highlightbackground="#d9d9d9")
        # self.Text1_19.configure(highlightcolor="black")
        # self.Text1_19.configure(insertbackground="black")
        # self.Text1_19.configure(selectbackground="#c4c4c4")
        # self.Text1_19.configure(selectforeground="black")
        # self.Text1_19.configure(undo="1")
        # self.Text1_19.configure(wrap="word")

        # self.Text1_20 = tk.Text(self.Labelframe2)
        # self.Text1_20.place(relx=0.446, rely=0.519, relheight=0.178
        #                     , relwidth=0.052, bordermode='ignore')
        # self.Text1_20.configure(background="white")
        # self.Text1_20.configure(font="TkTextFont")
        # self.Text1_20.configure(foreground="black")
        # self.Text1_20.configure(highlightbackground="#d9d9d9")
        # self.Text1_20.configure(highlightcolor="black")
        # self.Text1_20.configure(insertbackground="black")
        # self.Text1_20.configure(selectbackground="#c4c4c4")
        # self.Text1_20.configure(selectforeground="black")
        # self.Text1_20.configure(undo="1")
        # self.Text1_20.configure(wrap="word")

        # self.Text1_21 = tk.Text(self.Labelframe2)
        # self.Text1_21.place(relx=0.508, rely=0.519, relheight=0.178
        #                     , relwidth=0.052, bordermode='ignore')
        # self.Text1_21.configure(background="white")
        # self.Text1_21.configure(font="TkTextFont")
        # self.Text1_21.configure(foreground="black")
        # self.Text1_21.configure(highlightbackground="#d9d9d9")
        # self.Text1_21.configure(highlightcolor="black")
        # self.Text1_21.configure(insertbackground="black")
        # self.Text1_21.configure(selectbackground="#c4c4c4")
        # self.Text1_21.configure(selectforeground="black")
        # self.Text1_21.configure(undo="1")
        # self.Text1_21.configure(wrap="word")

        # self.Text1_22 = tk.Text(self.Labelframe2)
        # self.Text1_22.place(relx=0.569, rely=0.519, relheight=0.178
        #                     , relwidth=0.052, bordermode='ignore')
        # self.Text1_22.configure(background="white")
        # self.Text1_22.configure(font="TkTextFont")
        # self.Text1_22.configure(foreground="black")
        # self.Text1_22.configure(highlightbackground="#d9d9d9")
        # self.Text1_22.configure(highlightcolor="black")
        # self.Text1_22.configure(insertbackground="black")
        # self.Text1_22.configure(selectbackground="#c4c4c4")
        # self.Text1_22.configure(selectforeground="black")
        # self.Text1_22.configure(undo="1")
        # self.Text1_22.configure(wrap="word")

        # self.Text1_23 = tk.Text(self.Labelframe2)
        # self.Text1_23.place(relx=0.631, rely=0.519, relheight=0.178
        #                     , relwidth=0.052, bordermode='ignore')
        # self.Text1_23.configure(background="white")
        # self.Text1_23.configure(font="TkTextFont")
        # self.Text1_23.configure(foreground="black")
        # self.Text1_23.configure(highlightbackground="#d9d9d9")
        # self.Text1_23.configure(highlightcolor="black")
        # self.Text1_23.configure(insertbackground="black")
        # self.Text1_23.configure(selectbackground="#c4c4c4")
        # self.Text1_23.configure(selectforeground="black")
        # self.Text1_23.configure(undo="1")
        # self.Text1_23.configure(wrap="word")

        # self.Text1_24 = tk.Text(self.Labelframe2)
        # self.Text1_24.place(relx=0.692, rely=0.519, relheight=0.178
        #                     , relwidth=0.052, bordermode='ignore')
        # self.Text1_24.configure(background="white")
        # self.Text1_24.configure(font="TkTextFont")
        # self.Text1_24.configure(foreground="black")
        # self.Text1_24.configure(highlightbackground="#d9d9d9")
        # self.Text1_24.configure(highlightcolor="black")
        # self.Text1_24.configure(insertbackground="black")
        # self.Text1_24.configure(selectbackground="#c4c4c4")
        # self.Text1_24.configure(selectforeground="black")
        # self.Text1_24.configure(undo="1")
        # self.Text1_24.configure(wrap="word")

        # self.Text1_25 = tk.Text(self.Labelframe2)
        # self.Text1_25.place(relx=0.754, rely=0.519, relheight=0.178
        #                     , relwidth=0.052, bordermode='ignore')
        # self.Text1_25.configure(background="white")
        # self.Text1_25.configure(font="TkTextFont")
        # self.Text1_25.configure(foreground="black")
        # self.Text1_25.configure(highlightbackground="#d9d9d9")
        # self.Text1_25.configure(highlightcolor="black")
        # self.Text1_25.configure(insertbackground="black")
        # self.Text1_25.configure(selectbackground="#c4c4c4")
        # self.Text1_25.configure(selectforeground="black")
        # self.Text1_25.configure(undo="1")
        # self.Text1_25.configure(wrap="word")

if __name__ == '__main__':
    Graphical_user_interface().setGui()
