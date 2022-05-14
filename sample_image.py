from fileinput import filename
import os
from tkinter import*
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
from matplotlib import image
from tkinter import ttk
import pymysql
import cv2


# ================ Generate data set or sample images========= 

class SampleImg:
    def __init__(self,root):
        # self.root = Tk()
        self.root = root
        self.root.title("Sample Collecting")
        self.root.geometry("1350x700+0+0")



        title = Label(self.root, text="Sample Data Collection",font=("aleo", 26), relief=GROOVE, bg="#c0eff2", fg="#0A6870")
        title.pack(side=TOP, fill=X)
        #  Samplebtn = Button(Manage_Driver_Frame,text="Take Sample", command=self.generate_dataset,fg="#0D8C8C",bg="white",font=("aleo",12,"bold"),width=6, height=1).grid(row=0,column=4,padx=10,pady=7)

        sample = Button(self.root,text="take sample",command=self.generate_dataset,fg="#0D8C8C",bg="white",font=("aleo",12,"bold"),width=10, height=1).place(x=80,y=100)

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
        messagebox.showinfo("Result", "Data Sample collection Complteted Successfully")


root = Tk()
obj = SampleImg(root)
root.mainloop()






