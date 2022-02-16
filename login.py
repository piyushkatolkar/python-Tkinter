import tkinter 
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

root=Tk()
root.title("Login")
root.geometry("1350x700+0+0")


def register_window():
    root.destroy()
    import registration

#======= variable=======
Username=StringVar()
Password=StringVar()

#====== DEFINE DATABASE ======

def database():
    a = Username.get()
    b = Password.get()
    #print("a,b")

    if Username.get()=="" or Password.get()=="":
        messagebox.showerror("Error","All fields are required")
        #  elif Username.get()=="piyush" and Password.get()=="123456":
        #  messagebox.showinfo("Welcome","User is successfully login !!")
    else:
        messagebox.showinfo("Welcome",f"{Username.get()} is successfully login !!")
        #  messagebox.showerror("Error","Invalid Username or Password")

        root.destroy()
        import homepage


#====== Database =============

    conn = sqlite3.connect('cloths.db')
    
    conn.execute('''INSERT INTO LOGIN(Username,
                                      Password)VALUES(?,?)''',(a,b))
    conn.commit()
    conn.close()

#==== BG IMAGE ========
bg=ImageTk.PhotoImage(file="images/login.jpg")
bg_image=Label(root, image=bg)
bg_image.place(x=0,y=0,relwidth=1,relheight=1)

#==== Login Frame =====
Frame_login=Frame(root,bg="black")
Frame_login.place(x=180,y=200,height=350,width=470)


    
Label(root, text="CLOTHING STORE", font=("times new roman",30,"bold"),bg="black", fg="red",bd=10).place(x=5,y=5)
title = Label(root, text="Login", font=("times new roman",30,"bold"),bg="black", fg="grey",bd=10)
title.place(x=300,y=200)

#username
username = Label(root, text="Username : ", font=("times new roman",20,"bold"), bg="black", fg="grey",bd=10)
username.place(x=250,y=270)
Username = Entry(root, textvariable=Username, font=("times new roman",20,"bold"), fg="black",bd=5)
Username.place(x=250,y=320)

#password
password = Label(root, text=" Password : ", font=("times new roman",20,"bold"),bg="black", fg="grey",bd=10)
password.place(x=250,y=370)
Password = Entry(root, textvariable=Password, font=("times new roman",20,"bold"), fg="black",bd=5)
Password.place(x=250,y=420)

btnreg = Button(root, text=" Register a new account", cursor="hand2" ,font=("times new roman",10,"bold"), fg="light grey", bg="black",relief=FLAT, command=register_window)
btnreg.place(x=250,y=470)

login = Button(root, text="Login", cursor="hand2", font=("times new roman",15,"bold"),bg="black",fg="grey", relief=GROOVE, command=database)
login.place(x=330,y=500)


root.mainloop()