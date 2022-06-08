import os
from tkinter import*
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
from matplotlib import image
import numpy as np
import cv2



class train_data:
    def __init__(self,root):
        self.root=root
        self.root.title("Train Data Sample")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Train Data Sample",font=("aleo", 26, "bold"), relief=GROOVE, bg="#c0eff2", fg="#0A6870")
        title.place(x=0,y=150,width=1450,height=50)

        #left image
        root.left=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/tarin_sample1.jpg")
        left=Label(root,image=root.left).place(x=0,y=0,width=380,height=150)


        #middle image
        root.middle=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/train_sample2.png")
        middle=Label(root,image=root.middle).place(x=380,y=0,width=550,height=150)

        #right image
        root.right=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/train_sample 3.png")
        right=Label(root,image=root.right).place(x=930,y=0,width=500,height=150)

        # bg_full_image
        root.bg_train_set=ImageTk.PhotoImage(file="C:/Users/Data/Desktop/Project Work/code file/images/train_sample_bg.png")
        bg_train_set=Label(root,image=root.bg_train_set).place(x=0,y=200,width=1350,height=700)


        btn_Train=Button(root,text="Train Sample" ,cursor="hand2",fg="white",bg="#0A6870",font=("aleo",22,"bold"),command=self.train_classifier)
        btn_Train.place(x=600,y=500,width=260,height=70)




    def train_classifier(self):
        data_dir = ("sample_data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir) ] #list comprehension

        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L')  #grayscale conversion of image
            imageNp=np.array(img,'uint8')#datatype---unit8
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training Data", imageNp)
            cv2.waitKey(1)==13

        ids= np.array(ids)

        #=======Train Classifier and Save=============

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Data set Training completed Successfully!",parent=self.root)










if __name__ == "__main__":
    root=Tk()
    obj=train_data(root)
    root.mainloop()