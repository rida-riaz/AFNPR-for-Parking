from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD, ITALIC
import pymysql
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import cv2

class DriverRecord:
    def __init__(self,root):
        # self.root = Tk()
        self.root = root
        self.root.title("Driver's Record")
        self.root.geometry("1350x700+0+0")


        title = Label(self.root, text="Manage Driver's Record",font=("aleo", 26, "bold"), relief=GROOVE, bg="#c0eff2", fg="#0A6870")
        title.pack(side=TOP, fill=X)

        # Defining my variables==================

        self.driver_ID = StringVar()
        self.driver_name = StringVar()
        self.contact = StringVar()
        self.gender = StringVar()
        self.vehicle_no = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        

        # Manage_Driver_Frame====================
        Manage_Driver_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="#c0eff2")
        Manage_Driver_Frame.place(x=20, y=100,width=450, height=560)

        # Driver_Detail_Frame====================
        Driver_Detail_Frame = Frame(self.root, bd=3, relief=RIDGE, bg="#c0eff2")
        Driver_Detail_Frame.place(x=500, y=100,width=820, height=560)
        
        #feilds=============Manage_Driver_Frame
        detail_f_title = Label(Manage_Driver_Frame, text="Driver's Record",font=("aleo", 22, BOLD,ITALIC), bg="#c0eff2", fg="white")
        detail_f_title.grid(row=0,columnspan=2, pady=20)

        lbl_d_ID = Label(Manage_Driver_Frame, text="ID Number",font=("aleo", 16), bg="#c0eff2", fg="#0A6870")
        lbl_d_ID.grid(row=1,column=0, padx=10,pady=20,sticky="w")

        txt_ID = Entry(Manage_Driver_Frame,font=("aleo", 16), textvariable=self.driver_ID, bg="white", fg="#0A6870")
        txt_ID.grid(row=1,column=1, padx=10,pady=20,sticky="w")


        lbl_d_Name = Label(Manage_Driver_Frame, text="Driver Name",font=("aleo", 16), bg="#c0eff2", fg="#0A6870")
        lbl_d_Name.grid(row=2,column=0, padx=10,pady=20,sticky="w")

        txt_Name = Entry(Manage_Driver_Frame,font=("aleo", 16), textvariable=self.driver_name, bg="white", fg="#0A6870")
        txt_Name.grid(row=2,column=1, padx=10,pady=20,sticky="w")

        lbl_d_Vehicle_no = Label(Manage_Driver_Frame, text="Vehicle N0.",font=("aleo", 16), bg="#c0eff2", fg="#0A6870")
        lbl_d_Vehicle_no.grid(row=3,column=0, padx=10,pady=20,sticky="w")

        txt_Vehicle_no = Entry(Manage_Driver_Frame,font=("aleo", 16), textvariable=self.vehicle_no, bg="white", fg="#0A6870")
        txt_Vehicle_no.grid(row=3,column=1, padx=10,pady=20,sticky="w")

        lbl_d_gender=Label(Manage_Driver_Frame, text="Gender",font=("aleo", 16), bg="#c0eff2", fg="#0A6870")
        lbl_d_gender.grid(row=4,column=0, padx=10,pady=20,sticky="w")

        d_gender=ttk.Combobox(Manage_Driver_Frame,font=("aleo",15), textvariable=self.gender, state="readonly")
        d_gender['values'] = ("Select", "Male", "Female")
        d_gender.grid(row=4,column=1, padx=10,pady=20,sticky="w")

        lbl_d_Contact = Label(Manage_Driver_Frame, text="Contact",font=("aleo", 16), bg="#c0eff2", fg="#0A6870")
        lbl_d_Contact.grid(row=5,column=0, padx=10,pady=20,sticky="w")

        txt_Contact = Entry(Manage_Driver_Frame,font=("aleo", 16), textvariable=self.contact, bg="white", fg="#0A6870")
        txt_Contact.grid(row=5,column=1, padx=10,pady=20,sticky="w")

        # buttons_Frame====================
        button_Frame = Frame(Manage_Driver_Frame, bd=1, relief=RIDGE, bg="#c0eff2")
        button_Frame.place(x=10, y=450,width=420,height=50)

        Addbtn = Button(button_Frame,text="Register",command=lambda: self.Add_driver(),fg="#0D8C8C",bg="white",font=("aleo",12,"bold"),width=10, height=1).grid(row=0,column=0,padx=10,pady=7)

        Updatebtn = Button(button_Frame,text="Update",command=self.Update_data,fg="#0D8C8C",bg="white",font=("aleo",12,"bold"),width=7, height=1).grid(row=0,column=1,padx=10,pady=7)

        Deletebtn = Button(button_Frame,text="Delete",command=self.Delete_data,fg="#0D8C8C",bg="white",font=("aleo",12,"bold"),width=7, height=1).grid(row=0,column=2,padx=10,pady=7)

        Clearbtn = Button(button_Frame,text="Clear", command=self.clear,fg="#0D8C8C",bg="white",font=("aleo",12,"bold"),width=6, height=1).grid(row=0,column=3,padx=10,pady=7)

        TakePhotoSamplebtn = Button(Manage_Driver_Frame,text="Take Photo Sample", command=self.generate_dataset,fg="#0D8C8C",bg="white",font=("aleo",12,"bold"))
        TakePhotoSamplebtn.place(x=120, y=510,width=200,height=30)

       

       # search ===============
        
        lbl_Search = Label(Driver_Detail_Frame, text="Serach By",font=("aleo", 16), bg="#c0eff2", fg="#0A6870")
        lbl_Search.grid(row=0,column=0, padx=20,pady=20,sticky="w")

        com_search=ttk.Combobox(Driver_Detail_Frame,textvariable=self.search_by,font=("aleo",15), state="readonly", width=10)
        com_search['values'] = ("Driver_ID", "Driver_Name", "Vehicle_Number")
        com_search.grid(row=0,column=1, padx=30,pady=20,sticky="w")

        txt_search_item = Entry(Driver_Detail_Frame,textvariable=self.search_txt,font=("aleo", 16), width=14)
        txt_search_item.grid(row=0,column=2, padx=10,pady=20,sticky="w")

        serachbtn = Button(Driver_Detail_Frame,command=self.search_data,text="Search",fg="#0D8C8C",bg="white",font=("aleo",12,"bold"),width=10, height=1).grid(row=0,column=3, padx=15,pady=20,sticky="w")
        showbtn = Button(Driver_Detail_Frame,command=self.fetch_data,text="Show All",fg="#0D8C8C",bg="white",font=("aleo",12,"bold"),width=10, height=1).grid(row=0,column=4, padx=5,pady=20,sticky="w")

        # Table Frame==================================

        Table_Frame = Frame(Driver_Detail_Frame, bd=3, relief=RIDGE, bg="#c0eff2")
        Table_Frame.place(x=20, y=90,width=770, height=450)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.driver_record_table = ttk.Treeview(Table_Frame,columns=("ID","Driver's Name", "Contact", "Vehicle number","Gender","Flag"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.configure(command=self.driver_record_table.xview)
        scroll_y.configure(command=self.driver_record_table.yview)
        self.driver_record_table.heading("ID", text= "ID")
        self.driver_record_table.heading("Driver's Name", text= "Driver's Name")
        self.driver_record_table.heading("Contact", text= "Contact No.")
        self.driver_record_table.heading("Vehicle number", text= "Vehicle number")
        self.driver_record_table.heading("Gender", text= "Gender")
        self.driver_record_table.heading("Flag", text= "Visitor/Non Visitor")
        self.driver_record_table['show'] = 'headings'
        self.driver_record_table.column("ID", width=100)
        self.driver_record_table.column("Driver's Name", width=100)
        self.driver_record_table.column("Contact", width=100)
        self.driver_record_table.column("Vehicle number", width=100)
        self.driver_record_table.column("Gender", width=100)
        self.driver_record_table.column("Flag", width=100)
        self.driver_record_table.pack(fill= BOTH,expand=1)
        self.driver_record_table.bind("<ButtonRelease-1>", self.get_data)
        self.fetch_data()
        # self.root.mainloop()
        
        

    # def Add_driver(self):
    #     con = pymysql.connect(host="localhost", user="root", password="", database="afnpr system")
    #     cursor=con.cursor()
    #     cursor.execute("insert into manage_drivers values(%s,%s,%s,%s)",
    #                     (
    #                         self.driver_name.get(),
    #                         self.contact.get(),
    #                         self.vehicle_no.get(),
    #                         self.gender.get()  
    #                   # ) )

            # con.commit()
            # con.close() 
            # import Registration_form
            # Registration_form.Register()
    
    
    def Add_driver(self):
        root = Toplevel()
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
        con = pymysql.connect(host="localhost", user="root", password="", database="afnpr system")
        cursor=con.cursor()
        cursor.execute("select * from Driver_Registration_form")
        rows = cursor.fetchall()
                
        if self.text_fname.get()=="" or self.text_contact.get()=="" or self.text_veh_no.get()=="" or self.cmb_gender.get()=="Select" :
            messagebox.showerror("Error","All Feilds Required", parent = self.root)
        # elif len(rows)!= 0:
        #     for row in rows:
        #         if self.text_veh_no.get()== row[3]:
        #             messagebox.showerror("Error","This Vehicle Already Exist", parent = self.root)
        else:
            try:
                # con =   pymysql.connect(host="localhost", user="root", password="", database="afnpr system")
                # cursor=con.cursor()
                cursor.execute("insert into Driver_Registration_form(Driver_Name, Contact, Vehicle_Number, Gender, Flag_Value)values(%s,%s,%s,%s,%s)",
                                (
                                    self.text_fname.get(),
                                    self.text_contact.get(),
                                    self.text_veh_no.get(),
                                    self.cmb_gender.get(),
                                    self.var_chk.get()
                                ) )

                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success","Register successfully", parent = self.root)


            except Exception as es:
                messagebox.showerror("Error",f"Error due  to: {str(es)}", parent = self.root)
            
            # elif self.var_chk.get()== 0 or self.var_chk.get()== 1:
            #     messagebox.showerror("Error","assign Flag", parent = self.root)
            # elif self.img_path.get() == "None":
            #     messagebox.showwarning("Error","Please select image", parent = self.root)

                       
        


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="afnpr system")
        cursor=con.cursor()
        cursor.execute("select * from Driver_Registration_form")
        rows = cursor.fetchall()   
        if len(rows)!= 0:
            self.driver_record_table.delete(*self.driver_record_table.get_children())
            for row in rows:
                self.driver_record_table.insert('',END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.driver_ID.set("")
        self.driver_name.set("")
        self.vehicle_no.set("")
        self.contact.set("")
        self.gender.set("")

    def get_data(self,ev):
        cursor_row= self.driver_record_table.focus()
        contents = self.driver_record_table.item(cursor_row)
        row = contents['values']
        self.driver_ID.set(row[0])
        self.driver_name.set(row[1])
        self.contact.set(row[2])
        self.vehicle_no.set(row[3])
        self.gender.set(row[4])

    def Update_data(self):
        
        if self.driver_ID=="" or self.driver_name.get()=="" or self.contact.get()=="" or self.vehicle_no.get()=="" or self.gender.get()=="Select" :
            messagebox.showerror("Error","Select Data to Update", parent = self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update this driver's detail?", parent=self.root)
                if Update>0:
                    con =   pymysql.connect(host="localhost", user="root", password="", database="afnpr system")
                    cursor=con.cursor()
                    cursor.execute("update Driver_Registration_form set Driver_Name=%s, Contact=%s, Gender=%s, Vehicle_Number=%s where Driver_ID=%s",
                                (
                                    self.driver_name.get(),
                                    self.contact.get(),
                                    self.gender.get(),
                                    self.vehicle_no.get(),
                                    self.driver_ID.get()
                            ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Driver's Details Updated Successfully!", parent = self.root)
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error due  to: {str(es)}", parent = self.root)

        
        
        

    def Delete_data(self):
        if self.driver_ID=="":
            messagebox.showerror("Error","Driver's ID is Required, please select driver!", parent = self.root)
        else:
            try:
                Delete = messagebox.askyesno("Delete Detail","Do you want to Delete this driver's detail?", parent=self.root)
                if Delete>0:
                        con = pymysql.connect(host="localhost", user="root", password="", database="afnpr system")
                        cursor=con.cursor()
                        cursor.execute("delete from Driver_Registration_form where Driver_ID=%s",self.driver_ID.get())

                else:
                    if not Delete:
                        return
               
                con.commit()
                con.close()
                self.fetch_data()
                self.clear()
                messagebox.showinfo("Success","Driver's Details Deleted Successfully!", parent = self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Error due  to: {str(es)}", parent = self.root)

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="afnpr system")
        cursor=con.cursor()
        cursor.execute("select * from Driver_Registration_form where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cursor.fetchall()
        if len(rows)!= 0:
            self.driver_record_table.delete(*self.driver_record_table.get_children())
            for row in rows:
                self.driver_record_table.insert('',END, values=row)
            con.commit()
        con.close()





    def generate_dataset(self):
        con =   pymysql.connect(host="localhost", user="root", password="", database="afnpr system")
        cursor=con.cursor()
        cursor.execute("Select * from driver_registration_form")
        myresult = cursor.fetchall()
        id=0
        for x in myresult:
            id+=1
        cursor.execute("update Driver_Registration_form set Driver_Name=%s, Contact=%s, Gender=%s, Vehicle_Number=%s where Driver_ID=%s",
                            (
                                self.driver_name.get(),
                                self.contact.get(),
                                self.gender.get(),
                                self.vehicle_no.get(),
                                self.driver_ID.get()== id+1
                        ))

        con.commit()
        self.clear()
        con.close()    

        # =============== pre-define face data(harcascade) from opencv

        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        def face_cropped(img):
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces= face_classifier.detectMultiScale(gray,1.3,5) 
            # scaling factor= 1.3
            # min neighbour = 5

            for(x,y,w,h) in faces:
                face_cropped= img[y:y+h,x:x+w]
                return face_cropped

        cap = cv2.VideoCapture(0)
        img_id=0
        while True:
            ret,my_frame = cap.read()
            if face_cropped(my_frame) is not None:
                img_id+=1
                face= cv2.resize(face_cropped(my_frame),(450,450))
                face= cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                file_name_path= "sample_data/user."+str(id)+"."+str(img_id)+".jpg"
                cv2.imwrite(file_name_path,face)
                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
                cv2.imshow("Cropped face", face)
                

            if cv2.waitKey(1)==13 or int(img_id)==100:
                break
        
        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Data Sample collection Completed Successfully!")


    


if __name__ == "__main__":
    root = Tk()
    obj = DriverRecord(root)
    root.mainloop()

