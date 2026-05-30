import csv
from datetime import datetime
from tkinter import*
from tkinter import ttk
from tkinter import font
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import json
import numpy as np
from tkinter import filedialog




mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


#===================variables=========================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()



        #first image
        img_top=Image.open(r"college_image\background image.jpg")
        img_top=img_top.resize((800,200), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=800,height=200)



        #second image
        img_bottom=Image.open(r"college_image\background image.jpg")
        img_bottom=img_bottom.resize((800,200), Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=800,y=0,width=800,height=200)



         #background image
        img3=Image.open(r"college_image\background image.jpg")
        img3=img3.resize((1530,710), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

         #left lebel frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"college_image\background image.jpg")
        img_left=img_left.resize((720,130), Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        #label and entry
        # attendance ID
        attendenceID_lebel=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendenceID_lebel.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendenceID_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),textvariable=self.var_atten_id)
        attendenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #roll number
        rollNumber_lebel=Label(left_inside_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
        rollNumber_lebel.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        rollNumber_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),textvariable=self.var_atten_roll)
        rollNumber_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         # Student name
        studentName_lebel=Label(left_inside_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_lebel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),textvariable=self.var_atten_name)
        studentName_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #date
        date_lebel=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_lebel.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        date_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),textvariable=self.var_atten_date)
        date_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Department
        dep_lebel=Label(left_inside_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_lebel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        dep_combo=ttk.Combobox(left_inside_frame,width=18,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #time
        time_lebel=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_lebel.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        time_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",12,"bold"),textvariable=self.var_atten_time)
        time_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #attendance status
        attendenceStatus_lebel=Label(left_inside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
        attendenceStatus_lebel.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        attendenceStatus_combo=ttk.Combobox(left_inside_frame,width=18,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
        attendenceStatus_combo["values"]=("Status","Present","Absent")  
        attendenceStatus_combo.current(0)
        attendenceStatus_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=725,height=35)

        # Configure columns to have equal weight for equal distribution
        btn_frame.columnconfigure(0, weight=1)
        btn_frame.columnconfigure(1, weight=1)
        btn_frame.columnconfigure(2, weight=1)
        btn_frame.columnconfigure(3, weight=1)


# ============import button=========================
        save_btn=Button(btn_frame,text="Import csv",command=self.import_csv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,sticky="nsew", padx=2, pady=2)

# ==========================export button===========================
        update_btn=Button(btn_frame,text="Export csv",command=self.export_csv,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,sticky="nsew", padx=2, pady=2)


# ==================================update button=========================
        delete_btn=Button(btn_frame,text="Update",font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,sticky="nsew", padx=2, pady=2)

    
# =============================reset button=========================
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,sticky="nsew", padx=2, pady=2)








         #right lebel frame============================
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)

         #button frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=0,y=5,width=700,height=455)

        # ================scroll bar table=========================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll Number")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


# ======================fetch data==========================
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)


# =========import csv=========================
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)


#=====================export csv=========================
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


#get cursor
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


#===========reset data=========================
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("Select Department")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")



if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()