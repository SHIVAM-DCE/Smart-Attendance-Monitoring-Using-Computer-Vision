from tkinter import*
from tkinter import ttk
from tkinter import font
from turtle import width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import json
import numpy as np

class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="Train Data SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

# top image
        img_top=Image.open(r"college_image\background image.jpg")
        img_top=img_top.resize((1530,325), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)



 # train button       
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",40,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)

#bottom image
        img_bottom=Image.open(r"college_image\background image.jpg")
        img_bottom=img_bottom.resize((1530,325), Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)


    def train_classifier(self):
        try:
            data_dir = "data"
            if not os.path.exists(data_dir):
                messagebox.showerror("Error", "Data folder not found", parent=self.root)
                return
            
            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.jpg')]

            if len(path) == 0:
                messagebox.showerror("Error", "No training images found. Please take photo samples first.", parent=self.root)
                return

            faces = []
            ids = []
            label_map = {}
            skipped_count = 0

            for image in path:
                try:
                    img = Image.open(image).convert('L')  # gray scale image
                    imageNp = np.array(img, 'uint8')
                    filename = os.path.split(image)[1]
                    parts = filename.split('.')
                    if len(parts) < 3:
                        continue
                    actual_id = int(parts[1])

                    # VERIFY STUDENT ID EXISTS IN DATABASE
                    conn = mysql.connector.connect(host="localhost", username="root", password="Shivam@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=%s", (actual_id,))
                    result = my_cursor.fetchone()
                    conn.close()
                    
                    if result is None:
                        # Student was deleted - skip this image
                        skipped_count += 1
                        continue

                    if actual_id not in label_map:
                        label_map[actual_id] = len(label_map)

                    label_id = label_map[actual_id]
                    faces.append(imageNp)
                    ids.append(label_id)
                    cv2.imshow("Training", imageNp)
                    if cv2.waitKey(1) == 13:
                        break
                except Exception as img_error:
                    print(f"Error processing image {image}: {img_error}")
                    continue

            if len(faces) == 0:
                messagebox.showerror("Error", "No valid training images", parent=self.root)
                return

            ids = np.array(ids)

            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")

            mapping_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "label_map.json")
            with open(mapping_path, "w") as f:
                json.dump({str(k): v for k, v in label_map.items()}, f)

            cv2.destroyAllWindows()
            skipped_msg = f"\nSkipped {skipped_count} images from deleted students" if skipped_count > 0 else ""
            messagebox.showinfo("Result", f"Training completed!\nTrained on {len(faces)} images from {len(label_map)} students{skipped_msg}")
        except Exception as e:
            messagebox.showerror("Error", f"Training failed: {e}", parent=self.root)
        


























if __name__ == "__main__":
    root=Tk()
    obj=train(root)
    root.mainloop()


