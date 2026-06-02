from tkinter import*
from tkinter import ttk, messagebox
import tkinter
from PIL import Image, ImageTk
from utils import resource_path
import os
from help import Help
from student import Student
from train import train
from face_recognition import Face_Recognition
from attendence import Attendance
from developer import Developer
from time import strftime
from datetime import datetime





class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.title("face Recogniton System")
        self.root.state('zoomed')
        self.root.update_idletasks()
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        self.root._saved_geometry = self.root.winfo_geometry()
        self.root._saved_state = self.root.state()

        # first image
        
        img=Image.open(resource_path("college_image/background image.jpg"))
        img=img.resize((510,130), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=510,height=130)


        # second image
        img1=Image.open(resource_path("college_image/background image.jpg"))
        img1=img1.resize((510,130), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=510,y=0,width=510,height=130)


        # third image
        img2=Image.open(resource_path("college_image/background image.jpg"))
        img2=img2.resize((1020,130), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1020,y=0,width=510,height=130)



        #background image
        img3=Image.open(resource_path("college_image/background image.jpg"))
        img3=img3.resize((1530,710), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="SMART ATTENDANCE MONITORING SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)



#=====================time========================
        def update_time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, update_time)

        lbl=Label(title_lbl,font=("times new roman",14,"bold"),bg="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        update_time()




        #student button
        img4=Image.open(resource_path("college_image/studentDetails.jpg"))
        img4=img4.resize((220,220), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=200,y=300,width=220,height=40)




        #detect face button
        img5=Image.open(resource_path("college_image/face_Recog.jpg"))
        img5=img5.resize((220,220), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Detect Face",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=500,y=300,width=220,height=40)





        #attendence face button
        img6=Image.open(resource_path("college_image/attendence.png"))
        img6=img6.resize((220,220), Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=800,y=300,width=220,height=40)





        #help button
        img7=Image.open(resource_path("college_image/help.jpg"))
        img7=img7.resize((220,220), Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=1100,y=300,width=220,height=40)





        #train face button
        img8=Image.open(resource_path("college_image/Train_Face.jpg"))
        img8=img8.resize((220,220), Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=375,width=220,height=220)

        b1_1=Button(bg_img,text="Train Face",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=200,y=575,width=220,height=40)




        #photo face button
        img9=Image.open(resource_path("college_image/photos.jpg"))
        img9=img9.resize((220,220), Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=375,width=220,height=220)

        b1_1=Button(bg_img,text="Photo Face",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=500,y=575,width=220,height=40)




        #developer button
        img10=Image.open(resource_path("college_image/developer.jpg"))
        img10=img10.resize((220,220), Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=375,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=800,y=575,width=220,height=40)




        #exit button
        img11=Image.open(resource_path("college_image/exit.jpg"))
        img11=img11.resize((220,220), Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=375,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=1100,y=575,width=220,height=40)


        

    def open_img(self):
         os.startfile("data")

    
    def iExit(self):
        exit_choice = messagebox.askyesno("Face Recognition","Are you sure you want to exit?",parent=self.root)
        if exit_choice:
            self.root.destroy()
        else:
            return


        # =========function btn===========
        

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


    def developer_data(self):
        self.root.update_idletasks()
        self.root._saved_geometry = self.root.winfo_geometry()
        self.root._saved_state = self.root.state()
        self.new_window = Developer(self.root)
        self.new_window.state('zoomed')
        self.new_window.focus_force()
        self.new_window.lift()

    
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

