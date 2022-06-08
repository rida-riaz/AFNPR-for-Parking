import os
from tkinter import*
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
from matplotlib import image
import numpy as np
import cv2
import pymysql
from time import strftime
from datetime import datetime



class face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.title("Face Recognition")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#0A6870")

        title = Label(self.root, text="Face Recognition",font=("aleo", 26, "bold"), relief=GROOVE, bg="#c0eff2", fg="#0A6870")
        title.place(x=0,y=0,width=1450,height=50)


        #left image

        root.left = ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/face recognition 2.webp")
        left=Label(root,image=root.left).place(x=0,y=50,width=850,height=600)

        #right image
        root.right=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/facial_recognition_system 3.jpg")
        right=Label(root,image=root.right).place(x=850,y=50,width=600,height=600)

        btn_Train=Button(root,text="Recognize",command=self.face_recog,cursor="hand2",fg="white",bg="#0A6870",font=("aleo",22,"bold"))
        btn_Train.place(x=1020,y=650,width=260,height=50)



    # ========driver=============
    def member(self,d,v_n):
        with open("memberfile.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry= line.split ((","))
                name_list.append(entry[0])

            if((d not in name_list) and  (v_n not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString  = now.strftime("%H:%M:%S")
                f.writelines(f"\n{d},{v_n},{d1},{dtString},Member")



    # face Recognition========

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))



                con = pymysql.connect(host="localhost", user="root", password="", database="afnpr system")
                cursor=con.cursor()
                cursor.execute("select Driver_Name from driver_registration_form where Driver_ID="+str(id))
                d=cursor.fetchone()
                # print(d)
                d="+".join(d)

                cursor.execute("select Vehicle_Number from driver_registration_form where Driver_ID="+str(id))
                v=cursor.fetchone()
                v="+".join(v)


                if confidence>77:
                    cv2.putText(img,f"Driver Name:{d}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    cv2.putText(img,f"Vehicle Number:{v}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                    # self.member(d,v_n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown/Not a Member", (x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255))

                coord = [x,y,w,y]

            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Driver",clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Driver Recognition",img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root=Tk()
    obj=face_recognition(root)
    root.mainloop()