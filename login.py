from cgitb import text
import email
from email.message import EmailMessage
from tkinter import messagebox
from tkinter import*
from tkinter.tix import WINDOW

from PIL import Image, ImageTk, ImageDraw


class Login:

    def __init__(self, root):
        self.root = root
        self.root.title("Admin Login")
        self.root.geometry("1199x650+100+50")
        root.bg = ImageTk.PhotoImage(
            file="C:/Users/Data/Desktop/Project Work/code file/admin pics/bgg.jpeg")
        bg = Label(root, image=root.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        self.root.resizable(False, False)
        root.left = ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/admin pics/left bar.png")
        left = Label(root, image=root.left).place(
            x=80, y=100, width=400, height=500)

        # FrAME###3
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=480, y=100, height=500, width=500)
        title = Label(Frame_login, text="Admin Login", font=(
            "aleo", 26, "bold", "italic"), bg="white", fg="#0A6870").place(x=90, y=30)
        lbl_user = Label(Frame_login,  text="Username", font=("aleo", 15),
                         bg="white", fg="#0D8C8C").place(x=90, y=140)
        self.txt_user = Entry(Frame_login, font=("aleo", 15), bg="#c0eff2")
        self.txt_user.place(x=90, y=170, width=350, height=35)
        ####password##
        lbl_pass = Label(Frame_login,  text="Password", font=("aleo", 15),
                         bg="white", fg="#0D8C8C").place(x=90, y=220)
        self.txt_pass = Entry(Frame_login, font=("aleo", 15), bg="#c0eff2")
        self.txt_pass.place(x=90, y=250, width=350, height=35)

        Login_btn = Button(Frame_login, command=self.login_function, activebackground="#00b8f8", text="Login",  height=1, width=13,
                           cursor="hand2", fg="#0D8C8C", bg="#c0eff2", font=(
                               "aleo", 12, "bold")).place(x=90, y=370)
        #Forget##
        forget_btn = Button(Frame_login, text="Forget Password?", command=lambda: self.fwindow(
        ), activebackground="#00b8f8", width=15, height=1, cursor="hand2", fg="#0D8C8C", bg="#c0eff2", font=(
            "aleo", 12, "bold")).place(x=280, y=370)

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

        ###USERNAME LABEL FOR FORGET PASSOWRD WINDOW###
        self.txt_user = Label(self.forgetwindow, text="Username",  font=(
            "aleo", 15), fg="white", bg="#0A6870")
        self.txt_user.place(x=160, y=110)
        self.entry3 = Entry(self.forgetwindow, font=("aleo", 15), bg="#c0eff2")
        self.entry3.place(x=160, y=140, width=260)

        #NEW PASSWORD LABEL FOR FORGET PASSWORD WINDOW##
        self.txt_user = Label(self.forgetwindow, text="New Password", font=(
            "aleo", 15), fg="white", bg="#0A6870")
        self.txt_user.place(x=160, y=210)
        self.entry4 = Entry(self.forgetwindow, font=("aleo", 15), bg="#c0eff2")
        self.entry4.place(x=160, y=240, width=260)
        ###CONFIRM PASSWoRD LABEL####

        self.txt_user = Label(self.forgetwindow, text="Confirm Password", font=(
            "aleo", 15), fg="white", bg="#0A6870")
        self.txt_user.place(x=160, y=310)
        self.entry5 = Entry(self.forgetwindow, font=(
            "aleo", 15), bg="#c0eff2")
        self.entry5.place(x=160, y=340, width=260)

        ####Button for Change Password##3#

        self.chbutton = Button(self.forgetwindow, text="Change Password", cursor="hand2", fg="#0D8C8C", bg="#c0eff2", font=(
            "aleo", 12, "bold"), bd=3, command=lambda: self.chpass(), activebackground="green")
        self .chbutton.place(x=160, y=410, width=260, height=40)
        #####DATABASE###

    # def logindata(self):
    #     con=pymysql.connect("localhost","root","")
    #     cur=con.cursor()
    #     cur.execute("")
    #     row=cur.fetchone()
    #     if row==None:
    #         messagebox.showerror("Warning", "user not found")
    #     else:
    #         messagebox.showinfo("success", "Login Successfull")

    # working on forget window

    # def chpass(self):
    #     if self.entry3.get == "" and self.entry4.get() == "" and self.get == "":
    #         messagebox.showerror("Warning, All fields are required")

    #     else:
    #         pass
    #          con = pymysql.connect("")
    #            cur=con.cursor()
    #            cur.execute("Update query" , (self.entry4.get(), self.entry3.get()))
    #            cur.commit()
    #            cur.close()
    #          messagebox.showinfo("Success", "password changed successfully")

    def login_function(self):
        if self.txt_pass.get() == "" or self.txt_user.get() == "":
            messagebox.showerror("Error", "Please Fill", parent=self.root)
        elif self.txt_pass.get() == "ah" and self.txt_user.get() == "ah":
            messagebox.showinfo(
                "Login Succeed", f"Welcome {self.txt_user.get()}", parent=self.root)
        else:
            messagebox.showinfo(
                "Error", "Incorrect Username and Password", parent=self.root)


root = Tk()
obj = Login(root)
root.mainloop()