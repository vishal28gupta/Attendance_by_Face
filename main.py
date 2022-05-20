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
    
    
    
    
    
#     video 6
# class name change as Face_Recognition
#write in line 7,from Face_recognition import Face_Recognition

cLass Face_Recognition:
    def_init_(self, root):
       self.root=root
       self.root.geometry("1530x790+0+0")
       self.root.title("face Recogniton System")

       title_lbl-Label(self.root, text="FACE RECOGNITION, font=("times new roman", 35 ,"bold"),bg="white",fg="green")
       title_lbl.place(x=0, y=0,width=1530,height=45)
# 1st here image change in below line,these images are taken from tranee function
       img_top=Image.open(r" college_images\facialrecognition.png")
       img_top=img_top.resize((650,700), Image.ANTIALIAS)
       self.photoimg_top=ImageTk.PhotoImage(img_top)

       f_lbl-Label(self.root, image=self.photoimg_top)
       f_lbl.place(x=0, y=55, width=650,height=700)

    #   2nd  image change here
       img_bottom-Image.open("college_images\opencv_face_reco_more_data.jpg")
       img_bottom=img_bottom.resize((950,700), Image.ANTIALIAS) 
       self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
       
       f_lbl=Label(self.root, image=self.photoimg_bottom) 
       f_lbl.place(x=650, y=55,width=950,height=700)

    #    button on 2nd image,above image

       b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
       b1_1.place(x=365,y=620,width=200,height=40)

    #    vid-start from ,14 min,
    # face recognition
       def face recog(self):
           def draw_boundray (ing, classifier, scaleFactor, minNeighbors, color, text, clf): 
               gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
               features classifier.detectMultiScale (gray_image, scaleFactor, minNeighbors)

               coord=[]

               for (x,y,w,h) in features:
                   cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 3) 
                   id, predict=clf.predict(gray_image[y:y+h, x:x+w]) 
                   confidence-int((108*(1-predict/300)))
                   
                   conn=mysql.connector.connect (host="localhost", username="root", password="Test@123",database="face_recognizer")
                   my_cursor=conn.cursor()

                   my_cursor.execute("select Name from student where Student_id="+str(id) 
                   n=my_cursor.fetchone()
                   n="+".join(n)

                   my_cursor.execute("select Roll from student where Student_id="+str(id) 
                   r=my_cursor.fetchone()
                   r="+".join(r)

                   my_cursor.execute("select Dep from student where Student_id="+str(id) 
                   d=my_cursor.fetchone()
                   d="+".join(d)

                   
                   if confidence>77:
                       cv2.putText(img,f"Roll:{r}",(x,y-55)cv2.FONT_HERSHEY_COMPLEX,0,8,(255,255,255),3)
                       cv2.putText(img,f"Name:{n}",(x,y-30)cv2.FONT_HERSHEY_COMPLEX,0,8,(255,255,255),3)
                       cv2.putText(img,f"Department:{d}",(x,y-5)cv2.FONT_HERSHEY_COMPLEX,0,8,(255,255,255),3)
                    else:
                        cv2.rectangle(img,(x, y), (x+w, y+h),(0,0,255), 3) 
                        cv2.putText(img, "Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX,0,8,(255,255,255),3)

                    coord=[x,y,w,y]

                return coord

            def recognize(img, clf, faceCascade): 
                coord=draw_boundray (img, faceCascade, 1.1, 10, (255,25,255), "Face",clf) 
                return img

            faceCascade=cv2.CascadeClassifier( "haarcascade_frontalface_default.xml") 
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap=cv2.VideoCapture (0)

            while True:
                ret,img=video_cap.read()
                img-recognize (img, clf, faceCascade)
                cv2.imshow("Welcome TO face Recognition", img)

                if cv2.waitKey(1)==13:
                    break
            video_cap.release()
            cv2.destroyAllwindows()
    # video 6 end..


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
