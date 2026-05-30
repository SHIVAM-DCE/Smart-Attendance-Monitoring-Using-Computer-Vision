from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk   #pip install Pillow
import mysql.connector

class Register_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.state('zoomed')


#===============variables=================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_cpass=StringVar()

#=================background image=================
        self.bg_image = Image.open(r"college_image\login_bg.png")
        self.bg_label = Label(self.root)
        self.bg_label.place(x=0,y=0,relwidth=1,relheight=1)
        self._resize_bg(self.root.winfo_screenwidth(), self.root.winfo_screenheight())

        self.root.bind("<Configure>", self._on_root_resize)




        #left image
        left_img = Image.open(r"college_image\register_left.png")
        left_img = left_img.resize((470, 550), Image.Resampling.LANCZOS)
        self.bg1 = ImageTk.PhotoImage(left_img)
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

#=================main frame=================
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

    #=========label & entry===========
    #first name
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        fname.place(x=50,y=100)

        self.txt_fname=Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"),bg="white")
        self.txt_fname.place(x=50,y=130,width=250)

    #last name
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)
        self.txt_lname=Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"),bg="white")
        self.txt_lname.place(x=370,y=130,width=250)

    #contact number
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        self.txt_contact=Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"),bg="white")
        self.txt_contact.place(x=50,y=200,width=250)

    #email
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        self.txt_email=Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"),bg="white")
        self.txt_email.place(x=370,y=200,width=250)

    #security question
        question=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
        question.place(x=50,y=240)

        self.cmb_question=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.cmb_question["values"]=("Select","Your Birth Place","Your friend Name","Your Pet Name")
        self.cmb_question.current(0)
        self.cmb_question.place(x=50,y=270,width=250)

    #answer
        answer=Label(frame,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        answer.place(x=370,y=240)
        self.txt_answer=Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"),bg="white")
        self.txt_answer.place(x=370,y=270,width=250)

    #password
        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        password.place(x=50,y=320)
        self.txt_password=Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"),bg="white")
        self.txt_password.place(x=50,y=350,width=250)   

    #confirm password
        cpassword=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        cpassword.place(x=370,y=320)
        self.txt_cpassword=Entry(frame,textvariable=self.var_cpass,font=("times new roman",15,"bold"),bg="white")
        self.txt_cpassword.place(x=370,y=350,width=250)

    #check button
        self.var_chk=IntVar()
        chk=Checkbutton(frame,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12,"bold"),bg="white")
        chk.place(x=50,y=400)

    #register button
      
        register_btn=Button(frame,text="Register",font=("times new roman",15,"bold"),bg="green",fg="white",activeforeground="white",activebackground="green",cursor="hand2",command=self.register_data)
        register_btn.place(x=50,y=450,width=250,height=35)
    #login button
        login_btn=Button(frame,text="Login",font=("times new roman",15,"bold"),bg="red",fg="white",activeforeground="white",activebackground="red",cursor="hand2")
        login_btn.place(x=370,y=450,width=250,height=35)

    #=================function declaration=================
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="Select":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password Should Be Same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms & Conditions",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Shivam@123",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT * FROM register WHERE email=%s", (self.txt_email.get(),))
                row=my_cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error","User Already Exist, Please Try Another Email",parent=self.root)
                else:
                    query=("insert into register values(%s,%s,%s,%s,%s,%s,%s)")
                    value=(self.txt_fname.get(),self.txt_lname.get(),self.txt_contact.get(),self.txt_email.get(),self.cmb_question.get(),self.txt_answer.get(),self.txt_password.get())
                    my_cursor.execute(query, value)
                    conn.commit()
                    messagebox.showinfo("Success","Register Successfully",parent=self.root)
                    self.clear()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"Unable to connect or save data: {e}", parent=self.root)
            finally:
                try:
                    if conn.is_connected():
                        conn.close()
                except Exception:
                    pass

    def clear(self):
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.cmb_question.current(0)
        self.var_securityA.set("")
        self.var_pass.set("")
        self.var_cpass.set("")
        self.var_chk.set(0)





        






    def _resize_bg(self, width, height):
        if width < 1 or height < 1:
            return
        resized = self.bg_image.resize((width, height), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(resized)
        self.bg_label.config(image=self.bg)
        self.bg_label.image = self.bg

    def _on_root_resize(self, event):
        if event.widget == self.root:
            self._resize_bg(event.width, event.height)


if __name__ == "__main__":
    root=Tk()
    app=Register_Window(root)
    root.mainloop()
