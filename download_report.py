from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD, ITALIC
import pymysql
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import pandas as pd
import xlsxwriter
import pyodbc
import xlwt
import pandas.io.sql as sql
from pymysql import*



class DownloadReport:
    def __init__(self,root):
        # self.root = Tk()
        self.root = root
        self.root.title("Download Report")
        self.root.geometry("1350x700+0+0")


        title = Label(self.root, text="Download Report",font=("aleo", 26, "bold"), relief=GROOVE, bg="#c0eff2", fg="#0A6870")
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

        Updatebtn = Button(button_Frame,text="Update",command=self.Update_data,fg="#0D8C8C",bg="white",font=("aleo",12,"bold"),width=10, height=1).grid(row=0,column=1,padx=10,pady=7)

        Deletebtn = Button(button_Frame,text="Delete",command=self.Delete_data,fg="#0D8C8C",bg="white",font=("aleo",12,"bold"),width=10, height=1).grid(row=0,column=2,padx=10,pady=7)

        Downloadbtn = Button(button_Frame,text="Download",command=self.download,fg="#0D8C8C",bg="white",font=("aleo",12,"bold"),width=12, height=1).grid(row=0,column=3,padx=10,pady=7)



        Table_Frame = Frame(Driver_Detail_Frame, bd=3, relief=RIDGE, bg="#c0eff2")
        Table_Frame.place(x=20, y=50,width=770, height=450)

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


    def download(self):

        con=connect(host="localhost", user="root", password="", database="afnpr system")
        # read the data
        df=sql.read_sql('select * from Driver_Registration_form',con)
        # print the data
        print(df)
        # export the data into the excel sheet
        #df.to_excel(sheet_name = "drivers-record.xlsx", header = True, index = False)
        with pd.ExcelWriter("drivers-record.xlsx", engine="xlsxwriter", options = {'strings_to_numbers': True, 'strings_to_formulas': False}) as writer:
                try:
                    df = pd.read_sql("Select * from driver_registration_form", con)
                    df.to_excel(writer, sheet_name = "drivers-record.xlsx", header = True, index = False)
                    messagebox.showinfo("Download", "Report Downloaded Succesfully",parent = self.root)
                except:
                    print("There is an error")


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



if __name__ == "__main__":
    root = Tk()
    obj = DownloadReport(root)
    root.mainloop()
