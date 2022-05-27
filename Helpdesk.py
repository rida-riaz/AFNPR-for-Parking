import os
from tkinter import*
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
#from matplotlib import image
from tkinter import ttk
import pymysql
from tkinter.font import BOLD, ITALIC


class Helpdesk:
    def __init__(self,root):
        self.root=root
        self.root.title("Help Desk")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title = Label(self.root, text="Help Desk",font=("aleo", 26, BOLD), relief=GROOVE, bg="#0A6870", fg="white")
        title.pack(side=TOP, fill=X)

        #left image
        root.left=ImageTk.PhotoImage(file="E:/FYP/images/helpdesk.jpg")
        left=Label(root,image=root.left).place(x=0,y=50)
        #Contacts frame
        frame1=Frame(self.root,bg="#0A6870")
        frame1.place(x=845,y=50,width=500,height=800)
        title=Label(frame1,text="Developer's Contacts",font=("aleo",26, "bold","italic"),bg="white" , fg="#0A6870").place(x=55,y=30)
        Dvlpr_name1=Label(frame1,text="Laraib Safdar:",font=("aleo",15) , fg="#0D8C8C").place(x=50,y=200)
        Dvlpr1_mail=Label(frame1,text="laraibsafdar96@gmail.com",font=("aleo",12), fg="#0D8C8C").place(x=230,y=253)
        Dvlpr_name2=Label(frame1,text=" Rida Riaz:",font=("aleo",15) , fg="#0D8C8C").place(x=50,y=300)
        Dvlpr2_mail=Label(frame1,text="Ridariaz82@gmail.com",font=("aleo",12), fg="#0D8C8C").place(x=230,y=353)
        Dvlpr_name3=Label(frame1,text="Hadia Abubakar:",font=("aleo",15) , fg="#0D8C8C").place(x=50,y=400)
        Dvlpr3_mail=Label(frame1,text="hadirakab940@gmail.com",font=("aleo",12), fg="#0D8C8C").place(x=230,y=453)
root=Tk()
obj=Helpdesk(root)
root.mainloop()