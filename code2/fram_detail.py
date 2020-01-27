from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('test')
# root.iconbitmap()
my_img=ImageTk.PhotoImage(Image.open("box/img1.png"))
my_label =Label(root,image=my_img)
my_label.pack()
# print(Image.open("img1.png"))

Button_quit = Button(root,text="Exit", command=root.quit)
Button_quit.pack()

root.mainloop()


