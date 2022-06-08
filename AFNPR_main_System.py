# from curses import panel
import os
from tkinter import*
from tkinter import filedialog
from PIL import Image,ImageTk
from matplotlib import image
from Admin_panel import DriverRecord
from training_dataset import train_data
from Face_Recognition import face_recognition
from download_report import DownloadReport
import numpy as np



class AFNPR:
    def __init__(self,root):
        self.root=root
        self.root.title("AFNPR System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #background
        root.bg=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/admin pics/bgg.jpeg")
        bg=Label(root,image=root.bg).place(x=0,y=0,relwidth=1,relheight=1)
       
        #manage drivers record image
        root.img1=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/driver 2.jpg")
        left=Label(root,image=root.img1,cursor="hand2")
        left.place(x=30,y=30,width=280,height=300)
        left.bind('<Button-1>', self.manage_driver_record)
        

        #face detection image
        root.img2=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/face detection .jpeg")
        left=Label(root,image=root.img2,cursor="hand2")
        left.place(x=350,y=30,width=280,height=300)
        left.bind('<Button-1>', self.face_detection)

        #number plate detection image
        root.img3=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/number plate detection .jpeg")
        left=Label(root,image=root.img3,cursor="hand2")
        left.place(x=670,y=30,width=280,height=300)
        left.bind('<Button-1>', self.number_plate_detection)

        #change password image
        root.img4=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/change password .jpeg")
        left=Label(root,image=root.img4,cursor="hand2")
        left.place(x=1000,y=30,width=280,height=300)
        left.bind('<Button-1>', self.change_password)

        #photo Sample image
        root.img5=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/Photo Sample.png")
        left=Label(root,image=root.img5,cursor="hand2")
        left.place(x=30,y=380,width=280,height=300)
        left.bind('<Button-1>', self.Display_Sample)

        #Train image
        root.img6=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/train sample.png")
        left=Label(root,image=root.img6,cursor="hand2")
        left.place(x=350,y=380,width=280,height=300)
        left.bind('<Button-1>', self.train_dataSample)

        #download record image
        root.img7=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/download report .jpeg")
        left=Label(root,image=root.img7,cursor="hand2")
        left.place(x=670,y=380,width=280,height=300)
        left.bind('<Button-1>', self.download_record)

        #logout image
        root.img8=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/Exit .jpeg")
        left=Label(root,image=root.img8,cursor="hand2")
        left.place(x=1000,y=380,width=280,height=300)
        left.bind('<Button-1>', self.logout)


    
    
    def Display_Sample(self,ev):

        os.startfile("sample_data")
    
    
    def manage_driver_record(self,ev):

        self.new_window = Toplevel(self.root)
        self.app = DriverRecord(self.new_window)


    def train_dataSample(self,ev):

        self.new_window = Toplevel(self.root)
        self.app = train_data(self.new_window)
    
    def face_detection(self,ev):
        self.new_window = Toplevel(self.root)
        self.app = face_recognition(self.new_window)

    def number_plate_detection(self,ev):
        # root = Toplevel()
        # import Admin_panel
        # Admin_panel.DriverRecord()
        print("i'm clicked")

    def change_password(self,ev):
        # root = Toplevel()
        # import Admin_panel
        # Admin_panel.DriverRecord()
        print("i'm clicked")
    
    def download_record(self,ev):
        self.new_window = Toplevel(self.root)
        self.app = DownloadReport(self.new_window)


    def logout(self,ev):
        # root = Toplevel()
        # import Admin_panel
        # Admin_panel.DriverRecord()
        print("i'm clicked")

if __name__ == "__main__":
    root=Tk()
    obj=AFNPR(root)
    root.mainloop()