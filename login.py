from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

from main import Face_Recognition_System     #pip install Pillow



def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()





class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.state('zoomed')


      


        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_new_pass = StringVar()

        self.bg_image = Image.open(r"college_image\login_bg.png")
        self.bg_label = Label(self.root)
        self.bg_label.place(x=0,y=0,relwidth=1,relheight=1)
        self._resize_bg(self.root.winfo_screenwidth(), self.root.winfo_screenheight())

        self.root.bind("<Configure>", self._on_root_resize)

        # top header images and title like main.py
        img_top1 = Image.open(r"college_image\background image.jpg")
        img_top1 = img_top1.resize((510,130), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)
        Label(self.root, image=self.photoimg_top1).place(x=0,y=0,width=510,height=130)

        img_top2 = Image.open(r"college_image\background image.jpg")
        img_top2 = img_top2.resize((510,130), Image.Resampling.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)
        Label(self.root, image=self.photoimg_top2).place(x=510,y=0,width=510,height=130)

        img_top3 = Image.open(r"college_image\background image.jpg")
        img_top3 = img_top3.resize((510,130), Image.Resampling.LANCZOS)
        self.photoimg_top3 = ImageTk.PhotoImage(img_top3)
        Label(self.root, image=self.photoimg_top3).place(x=1020,y=0,width=510,height=130)

        title_lbl=Label(self.root,text="SMART ATTENDANCE MONITORING SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=130,width=1530,height=45)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=200,width=340,height=450)

        img1=Image.open(r"college_image\username.jpg")
        img1=img1.resize((100,100), Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1) 
        lblimg1=Label(image=self.photoimg1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=210,width=100,height=100)
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=110)


        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        #label
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=250,width=270)



        #==============icon images=================
        img2=Image.open(r"college_image\username.jpg")
        img2=img2.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=355,width=25,height=25)

        img3=Image.open(r"college_image\password.png")
        img3=img3.resize((25,25), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimg3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=425,width=25,height=25)

        #login button
        login_btn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bg="red",fg="white",activeforeground="white",activebackground="red",cursor="hand2")
        login_btn.place(x=119,y=300,width=100,height=35)

        #==============register button=================
        register_btn=Button(frame,text="Create New Account",command=self.register,font=("times new roman",12,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black",cursor="hand2")
        register_btn.place(x=20,y=350,width=160,height=35)

            #==============forgot password button=================  
        forgot_btn=Button(frame,text="Forgot Password",command=self.forget_password,font=("times new roman",12,"bold"),borderwidth=0,bg="black",fg="white",activeforeground="white",activebackground="black",cursor="hand2")
        forgot_btn.place(x=9,y=380,width=160,height=25)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txtuser.get()=="admin" and self.txtpass.get()=="admin":
            messagebox.showinfo("Success","Welcome to Face Recognition Attendance System",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shivam@123",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin",parent=self.root)
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
                
                conn.commit()
                conn.close()  



    def forget_password(self):  
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Shivam@123",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s", (self.txtuser.get(),))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel(self.root)
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                self.root2.transient(self.root)
                self.root2.grab_set()

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                #security question
                question=Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="white",fg="black")
                question.place(x=50,y=80)

                self.cmb_question=ttk.Combobox(self.root2,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
                self.cmb_question["values"]=("Select","Your Birth Place","Your friend Name","Your Pet Name")
                self.cmb_question.current(0)
                self.cmb_question.place(x=50,y=110,width=250)

                #answer
                answer=Label(self.root2,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                answer.place(x=50,y=150)
                self.txt_answer=Entry(self.root2,textvariable=self.var_securityA,font=("times new roman",15,"bold"),bg="white")
                self.txt_answer.place(x=50,y=180,width=250)

                #new password
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)
                self.txt_new_password=Entry(self.root2,textvariable=self.var_new_pass,font=("times new roman",15,"bold"),bg="white",show="*")
                self.txt_new_password.place(x=50,y=250,width=250)

                reset_btn=Button(self.root2,text="Reset Password",command=self.reset_password,font=("times new roman",13,"bold"),bg="green",fg="white",cursor="hand2")
                reset_btn.place(x=50,y=300,width=250,height=35)

    def reset_password(self):
        if self.cmb_question.get() == "Select":
            messagebox.showerror("Error","Please select a security question",parent=self.root2)
            return
        if self.var_securityA.get() == "":
            messagebox.showerror("Error","Please enter the security answer",parent=self.root2)
            return
        if self.var_new_pass.get() == "":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
            return
        try:
            conn = mysql.connector.connect(host="localhost",user="root",password="Shivam@123",database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s",(
                self.txtuser.get(),
                self.var_securityQ.get(),
                self.var_securityA.get()
            ))
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error","Security question or answer is incorrect",parent=self.root2)
            else:
                my_cursor.execute("UPDATE register SET password=%s WHERE email=%s",(
                    self.var_new_pass.get(),
                    self.txtuser.get()
                ))
                conn.commit()
                messagebox.showinfo("Success","Password reset successfully",parent=self.root2)
                self.root2.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Unable to reset password: {e}", parent=self.root2)
        finally:
            try:
                if conn.is_connected():
                    conn.close()
            except Exception:
                pass

    def register(self):
        self.new_window=Toplevel(self.root)
        self.app=Register_Window(self.new_window)





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












#==================register window=================
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
        login_btn=Button(frame,text="Login",font=("times new roman",15,"bold"),bg="red",fg="white",activeforeground="white",activebackground="red",cursor="hand2",command=self.back_to_login)
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

    def back_to_login(self):
        self.root.destroy()

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
    main()       

