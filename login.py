from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD, ITALIC
import pymysql
import os
import numpy as np
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
from AFNPR_main_System import AFNPR
from matplotlib import image
from Admin_panel import DriverRecord
from training_dataset import train_data
from Face_Recognition import face_recognition
from download_report import DownloadReport



class Login:
    def __init__(self,root):
        self.root = root
        self.login_form()
   
    def login_form(self):
        self.root = root
        self.root.title("Admin Login")
        self.root.geometry("1350x700+0+0")
       
        root.bg = ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/admin pics/bgg.jpeg")
        bg = Label(root, image=root.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # self.root.resizable(False, False)
       
      
        root.left = ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/admin pics/left bar.png")
        left = Label(root, image=root.left).place(x=240, y=100, width=400, height=500)
    
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=630, y=100, height=500, width=500)
        title = Label(Frame_login, text="Admin Login", font=(
            "aleo", 26, "bold", "italic"), bg="white", fg="#0A6870").place(x=90, y=30)
        lbl_user = Label(Frame_login,  text="Username", font=("aleo", 15),
                         bg="white", fg="#0D8C8C").place(x=90, y=140)
        self.txt_user = Entry(Frame_login, font=("aleo", 15), bg="#c0eff2")
        self.txt_user.place(x=90, y=170, width=350, height=35)
        ####password##
        lbl_pass = Label(Frame_login,  text="Password",  font=("aleo", 15),
                         bg="white", fg="#0D8C8C").place(x=90, y=220)
        self.txt_pass = Entry(Frame_login, font=("aleo", 15), show="*", bg="#c0eff2")
        self.txt_pass.place(x=90, y=250, width=350, height=35)

        Login_btn = Button(Frame_login, command=self.login_function, activebackground="#00b8f8", text="Login",  height=1, width=13,
                           cursor="hand2", fg="#0D8C8C", bg="#c0eff2", font=(
                               "aleo", 13, "bold")).place(x=90, y=370)
        #Forget##
        forget_btn = Button(Frame_login, text="Forget Password?", command=lambda: self.fwindow(
        ), activebackground="#00b8f8", width=15, height=1, cursor="hand2", fg="#0D8C8C", bg="#c0eff2", font=(
            "aleo", 13, "bold")).place(x=280, y=370)
        R_btn = Button(Frame_login, text="Not Registered yet? Register Now", command=lambda: self.Register_form(
        ), activebackground="#00b8f8", width=30, height=1, cursor="hand2", fg="#0D8C8C", bg="#c0eff2", font=(
            "aleo", 13, "bold")).place(x=110, y=430)
        
       
       
    #Forget Window##

    def fwindow(self):

        forgetwindow = Toplevel()

        self.forgetwindow = forgetwindow
        self.forgetwindow.title("Forget Password")
        self.forgetwindow.geometry("600x500+350+150")
        forgetwindow.config(bg="#0A6870")
        title = Label(forgetwindow, text="Forget Password", font=(
            "aleo", 26, "bold", "italic"), fg="white", bg="#0A6870").place(x=150, y=30)

        self.forgetwindow.resizable(False, False)

        # =========USERNAME LABEL FOR FORGET PASSOWRD WINDOW======================
        self.txt_user = Label(self.forgetwindow, text="Email",  font=(
            "aleo", 15), fg="white", bg="#0A6870")
        self.txt_user.place(x=160, y=110)
        self.entry3 = Entry(self.forgetwindow, font=("aleo", 15), bg="#c0eff2")
        self.entry3.place(x=160, y=140, width=260)

        #NEW PASSWORD LABEL FOR FORGET PASSWORD WINDOW==========================
        self.txt_user = Label(self.forgetwindow, text="New Password", font=(
            "aleo", 15), fg="white", bg="#0A6870")
        self.txt_user.place(x=160, y=210)
        self.entry4 = Entry(self.forgetwindow, show="*", font=("aleo", 15), bg="#c0eff2")
        self.entry4.place(x=160, y=240, width=260)
        ###CONFIRM PASSWoRD LABEL####

        self.txt_user = Label(self.forgetwindow, text="Confirm Password", font=(
            "aleo", 15), fg="white", bg="#0A6870")
        self.txt_user.place(x=160, y=310)
        self.entry5 = Entry(self.forgetwindow, show="*", font=(
            "aleo", 15), bg="#c0eff2")
        self.entry5.place(x=160, y=340, width=260)

        ####Button for Change Password##3#

        self.chbutton = Button(self.forgetwindow, text="Change Password", cursor="hand2", fg="#0D8C8C", bg="#c0eff2", font=(
            "aleo", 12, "bold"), bd=3, command=lambda: self.chpass(), activebackground="green")
        self .chbutton.place(x=160, y=410, width=260, height=40)
        #####DATABASE###


    # working on forget window

    def chpass(self):
        if self.entry3.get() == "" and self.entry4.get() == "" and self.entry5.get() == "":
            messagebox.showerror("Warning", "All fields are required")

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="afnpr system")
                cur = con.cursor()
                if self.entry4.get() == self.entry5.get():
                    
                    cur.execute("UPDATE register_admin SET Admin_password=%s, Admin_Con_Pass=%s WHERE Admin_Email=%s", (
                    self.entry4.get(), 
                    self.entry5.get(), 
                    self.entry3.get()
                    ))
                    con.commit()
                    cur.close()
                    messagebox.showinfo("Success", "password changed successfully")
                else:
                    messagebox.showerror("Sorry", "Password not match!", parent = self.root)
            except Exception as es:
                messagebox.showerror(
                    'Error', f"Error due to:{str(es)}", parent=self.root)

 ###LOgin backend###3
    def login_function(self):
        if self.txt_pass.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("Error", "Please Fill", parent=self.root)
        
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="afnpr system")
                cur = con.cursor()
                cur.execute('select * from register_admin where Ad_Username=%s and Admin_password=%s',
                            (self.txt_user.get(), self.txt_pass.get()))
                row = cur.fetchall()
               
                if row==None:
                     messagebox.showerror("Error", "User Not Found", parent=self.root)
                
               
              
                elif row:
                    messagebox.showinfo("Success", "Login successfull")
                    # self.root.destroy()
                    self.appscreen()
                    con.close()

                else:
                 messagebox.showerror("Error", "Invalid Username or Password")
            except Exception as es:
                messagebox.showerror('Error', f"Error due to:{str(es)}", parent=self.root)

       

    # Register frame============================
    def Register_form(self):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # background
        root.bg = ImageTk.PhotoImage(
            file="C:/Users/Data/Desktop/Project Work/code file/admin pics/bgg.jpeg")
        bg = Label(root, image=root.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        # left image
        root.left = ImageTk.PhotoImage(
            file="C:/Users/Data/Desktop/Project Work/code file/admin pics/left bar.png")
        left = Label(root, image=root.left).place(
            x=80, y=100, width=400, height=500)
            
        self.frame1 = Frame(self.root, bg="white")
        self.frame1.place(x=480, y=100, width=700, height=500)
        title = Label(self.frame1, text="Register Here", font=(
            "aleo", 26, "bold", "italic"), bg="white", fg="#0A6870").place(x=50, y=30)
        # first name----- row 1
        f_name = Label(self.frame1, text="Name", font=("aleo", 15),
                       bg="white", fg="#0D8C8C").place(x=50, y=90)
        self.text_fname = Entry(self.frame1, font=("aleo", 15), bg="#c0eff2")
        self.text_fname.place(x=50, y=120, width=250, height=35)
             # Username----- row 2
        f_Uname = Label(self.frame1, text="Username", font=("aleo", 15),
                        bg="white", fg="#0D8C8C").place(x=50, y=170)
        self.text_fUname = Entry(self.frame1, font=("aleo", 15), bg="#c0eff2")
        self.text_fUname.place(
            x=50, y=200, width=250, height=35)
             # contact----- row 3
        contact= Label(self.frame1, text="Contact No", font=(
            "aleo", 15), bg="white", fg="#0D8C8C").place(x=50, y=250)
        self.text_contact = Entry(self.frame1, font=("aleo", 15), bg="#c0eff2")
        self.text_contact.place(
            x=50, y=280, width=250, height=35)
        # Password----------row 1
        
        Email_id = Label(self.frame1, text="Email", font=("aleo", 15),
                          bg="white", fg="#0D8C8C").place(x=370, y=90)
        self.text_Email = Entry(self.frame1, font=("aleo", 15), bg="#c0eff2")
        self.text_Email.place(
            x=370, y=120, width=250, height=35)
             # confirm password----- row 2
        Password = Label(self.frame1, text="Password",  font=("aleo", 15),
                         bg="white", fg="#0D8C8C").place(x=370, y=170)
        self.text_Password = Entry(self.frame1, show="*", font=("aleo", 15), bg="#c0eff2")
        self.text_Password.place(
            x=370, y=200, width=250, height=35)

        
        # Gender--------------row 3
        CPassword= Label(self.frame1, text="Confirm Password", font=("aleo", 15),
                       bg="white", fg="#0D8C8C").place(x=370, y=250)
        self.text_CPassword = Entry(self.frame1, show="*", font=("aleo", 15), bg="#c0eff2")
        self.text_CPassword.place(
            x=370, y=280, width=250, height=35)
       

        # button---- register

        btn = Button(self.frame1, text="Register", command=lambda: self.register(), cursor="hand2", fg="#0D8C8C", bg="#c0eff2", font=(
            "aleo", 14, "bold")).place(x=60, y=370, width=230, height=50)
         # button---- Login
        btn2 = Button(self.frame1, text="Already Registered? Login Here", command=lambda:self.login_form(), cursor="hand2", fg="#0D8C8C", bg="#c0eff2", font=(
            "aleo", 12, "bold")).place(x=360, y=370, width=260, height=50)

    def register(self):
        if self.text_fname.get()=="" or self.text_fUname.get()=="" or self.text_Password.get()=="" or self.text_Email.get()=="" or self.text_CPassword.get()=="" or self.text_contact.get()=="":
            messagebox.showerror("Error", "All Fields Required", parent=self.root)
        elif self.text_Password.get()!= self.text_CPassword.get():
            messagebox.showerror("Error","Password and Confirm Password should be same", parent=self.root)
        else: 
            try:
                con=pymysql.connect(host="localhost", user="root", password="", database="afnpr system")
                cur=con.cursor()
                cur.execute("select * from register_admin  where Ad_Username=%s", self.text_fUname.get())
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("Error", "User Already Exist, Please try with other username",parent=self.root)
                else:
                     cur.execute("insert into register_admin values(%s, %s, %s, %s, %s, %s)",(self.text_fname.get(), self.text_fUname.get(), self.text_contact.get(), self.text_Email.get(), self.text_Password.get(), self.text_CPassword.get()))

                     con.commit()    
                     con.close()
                     messagebox.showinfo("Success","Register Successfull", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}", parent=self.root) 
    def appscreen(self):
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
    root = Tk()
    obj = Login(root)
    root.mainloop()