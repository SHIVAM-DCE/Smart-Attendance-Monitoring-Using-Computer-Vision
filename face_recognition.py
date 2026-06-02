from datetime import datetime
from tkinter import*
from tkinter import ttk
from tkinter import font
from turtle import width
from PIL import Image, ImageTk
from utils import resource_path
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import json
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

    #first image
        img_top=Image.open(resource_path("college_image/background image.jpg"))
        img_top=img_top.resize((650,700), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)



        #second image
        img_bottom=Image.open(resource_path("college_image/background image.jpg"))
        img_bottom=img_bottom.resize((950,700), Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)

        #button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="dark green",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)





    #=================attendance===============================================================
    def mark_attendance(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split(",")
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")







 #=================face recognition=================================================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int(max(0, min(100, (100*(1-predict/300)))))
                student_id = inv_label_map.get(id)

                if student_id is not None and confidence > 77:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Shivam@123",database="face_recognizer")
                    my_cursor=conn.cursor()

                    my_cursor.execute("select student_id from student where student_id=%s", (student_id,))
                    result = my_cursor.fetchone()
                    i = str(result[0]) if result and result[0] is not None else "Unknown"

                    my_cursor.execute("select name from student where student_id=%s", (student_id,))
                    result = my_cursor.fetchone()
                    n = str(result[0]) if result and result[0] is not None else "Unknown"

                    my_cursor.execute("select roll from student where student_id=%s", (student_id,))
                    result = my_cursor.fetchone()
                    r = str(result[0]) if result and result[0] is not None else "Unknown"

                    my_cursor.execute("select dep from student where student_id=%s", (student_id,))
                    result = my_cursor.fetchone()
                    d = str(result[0]) if result and result[0] is not None else "Unknown"
                    conn.close()

                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord=[x,y,w,h]

            return coord
        

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        label_map_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "label_map.json")
        inv_label_map = {}
        if os.path.exists(label_map_path):
            with open(label_map_path, "r") as f:
                label_map = json.load(f)
                inv_label_map = {int(v): int(k) for k, v in label_map.items()}
        video_cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not video_cap.isOpened():
            messagebox.showerror("Camera Error", "Camera not detected or cannot be opened. Please check your device.")
            return
        cv2.namedWindow("Welcome To Face Recognition", cv2.WINDOW_NORMAL)
        no_frame_count = 0
        while True:
            ret,img=video_cap.read()
            if not ret or img is None:
                no_frame_count += 1
                if no_frame_count > 30:
                    messagebox.showerror("Camera Error", "Camera opened but no video frames are being received. Close other camera apps and try again.")
                    break
                cv2.waitKey(100)
                continue
            no_frame_count = 0
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
        



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
