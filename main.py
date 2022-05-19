from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogniton System")

        # bg image
        img3=Image.open(r"D:\Face_Attendance_Clg\images\bgimg.jpg")
        img3=img3.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root, image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0,width=1530,height=45)

        # Student button
        img4=Image.open(r"D:\Face_Attendance_Clg\images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button (bg_img, text="Student Details", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300,width=220,height=40)

        # Face Recognition button
        img4=Image.open(r"D:\Face_Attendance_Clg\images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x=650,y=100,width=220,height=220)

        b1_1=Button (bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=650, y=300,width=220,height=40)

        # Attendance button
        img4=Image.open(r"D:\Face_Attendance_Clg\images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button (bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300,width=220,height=40)

        # Train Data button
        img4=Image.open(r"D:\Face_Attendance_Clg\images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button (bg_img, text="Train Data", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=600,width=220,height=40)

        # Photos button
        img4=Image.open(r"D:\Face_Attendance_Clg\images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x=650,y=400,width=220,height=220)

        b1_1=Button (bg_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=650, y=600,width=220,height=40)

        # Exit button
        img4=Image.open(r"D:\Face_Attendance_Clg\images\Subha.jpg")
        img4=img4.resize((220,220), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button (bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=600,width=220,height=40)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

    
    
    
    
    
    
    
    gdgd
