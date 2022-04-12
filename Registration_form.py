from optparse import Values
import os
from tkinter import*
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
from matplotlib import image
from tkinter import ttk
import pymysql


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Reigstration form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #background
        root.bg=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/admin pics/bgg.jpeg")
        bg=Label(root,image=root.bg).place(x=0,y=0,relwidth=1,relheight=1)
       
        #left image
        root.left=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/admin pics/left bar.png")
        left=Label(root,image=root.left).place(x=80,y=100,width=400,height=500)

        #Register frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        title=Label(frame1,text="Register Here...",font=("aleo",26, "bold","italic"),bg="white" , fg="#0A6870").place(x=50,y=30)
       
        #first name----- row 1
        Driver_name=Label(frame1,text="Name",font=("aleo",15),bg="white" , fg="#0D8C8C").place(x=50,y=100)
        self.text_fname=Entry(frame1,font=("aleo",15),bg="#c0eff2")
        self.text_fname.place(x=50,y=130,width=250,height=35)
        #contact
        contact=Label(frame1,text="Contact",font=("aleo",15),bg="white" , fg="#0D8C8C").place(x=370,y=100)
        self.text_contact=Entry(frame1,font=("aleo",15),bg="#c0eff2")
        self.text_contact.place(x=370,y=130,width=250,height=35)


        #vehicle number----- row 2
        vehicle_num=Label(frame1,text="Vehicle number",font=("aleo",15),bg="white" , fg="#0D8C8C").place(x=50,y=200)
        self.text_veh_no=Entry(frame1,font=("aleo",15),bg="#c0eff2")
        self.text_veh_no.place(x=50,y=230,width=250,height=35)
        #Gender
        Gender=Label(frame1,text="Gender",font=("aleo",15),bg="white" , fg="#0D8C8C").place(x=370,y=200)
        self.cmb_gender=ttk.Combobox(frame1,font=("aleo",15), state="readonly")
        self.cmb_gender['values'] = ("Select", "Male", "Female")
        self.cmb_gender.place(x=370,y=230,width=250,height=35)
        self.cmb_gender.current(0)
        #checkbox
        self.var_chk = IntVar()
        chk=Checkbutton(frame1,text="Assign flag to visitor", variable= self.var_chk,onvalue=1,offvalue=0,bg="white",font=("aleo",12)).place(x=50,y=300)
        #Upload Image
        # Driver_img=Label(frame1,text="Upload Driver's Image",font=("aleo",12,"bold"),bg="white" , fg="#0D8C8C").place(x=50,y=337)
        # btn_upload_img=Button(frame1,text="Upload" ,cursor="hand2",fg="#0D8C8C",bg="#c0eff2",font=("aleo",12,"bold"),command=self.show_img).place(x=240,y=337,width=100,height=28)
        btn_Register=Button(frame1,text="Register" ,cursor="hand2",fg="#0D8C8C",bg="#c0eff2",font=("aleo",12,"bold"),command=self.Register_Driver).place(x=200,y=400,width=230,height=40)


    # def show_img(self):
    #     global img_path 
    #     fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image", filetypes=(("JPG File", "*.jpg"),("PNG File", "*.png"),("All Files", "*.*")))
    #     img_path = fln
    #     self.var_flag = IntVar()
    #     self.var_flag = img_path

    #     self.label = ttk.LabelFrame(self.root, text = "")
    #     self.label.place(x=290,y=337)
    #     self.label.configure(text = self.fln)
    #     print(type(fln))
    #     print(fln)
        # img = Image.open(fln)
        # img = ImageTk.PhotoImage(img)
        # lbl.configure(image=img)
        # lbl.image = img

    def Register_Driver(self):
        if self.text_fname.get()=="" or self.text_contact.get()=="" or self.text_veh_no.get()=="" or self.cmb_gender.get()=="Select" :
            messagebox.showerror("Error","All Feilds Required", parent = self.root)
        # elif self.var_chk.get()== 0 or self.var_chk.get()== 1:
        #     messagebox.showerror("Error","assign Flag", parent = self.root)
        # elif self.img_path.get() == "None":
        #     messagebox.showwarning("Error","Please select image", parent = self.root)
        else:
            try:
                con =   pymysql.connect(host="localhost", user="root", password="", database="afnpr system")
                cursor=con.cursor()
                cursor.execute("insert into Driver_Registration_form(Driver_Name, Contact, Vehicle_Number, Gender, Flag_Value)values(%s,%s,%s,%s,%s)",
                                (
                                    self.text_fname.get(),
                                    self.text_contact.get(),
                                    self.text_veh_no.get(),
                                    self.cmb_gender.get(),
                                    self.var_chk.get()
                                ) )

                con.commit()
                con.close()
                messagebox.showinfo("Success","Register successfully", parent = self.root)


            except Exception as es:
                messagebox.showerror("Error",f"Error due  to: {str(es)}", parent = self.root)

            





    

root=Tk()
obj=Register(root)
# lbl = Label(root)
# lbl.pack()
root.mainloop()