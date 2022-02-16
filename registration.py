import tkinter
import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image


root=Tk()
root.title("Registration Form")
root.geometry("1350x700+0+0")

#==== CLIK LOGIN BUTTON TO JUMP LOGIN WINDOW ===============================================================

def login_window():
    root.destroy()
    import login

#======= variable=======
Full_name = StringVar()
Plot_no = StringVar()
Street = StringVar()
State = StringVar()
City = StringVar()
Pincode = StringVar()
Email = StringVar()
password = StringVar()
Mobile_no = StringVar()

#====== DEFINE DATABASE ======

def database():
    a = Full_name.get()
    b = Plot_no.get()
    c = Street.get()
    d = State.get()
    e = City.get()
    f = Pincode.get()
    g = Email.get()
    h = Password.get()
    i = Mobile_no.get()

    #print("a,b,c,d,e,f,g,h,i") # to show the user data in output

    if Full_name.get()=="" or Plot_no.get()=="" or Street.get()=="" or State.get()=="" or City.get()=="" or Pincode.get()=="" or Email.get()=="" or Password.get()=="" or Mobile_no.get()=="" :
        messagebox.showerror("Error","All fields are required")
    else:
        messagebox.showinfo("Welcome",f"{Full_name.get()} is successfully Register !!")

#====== Database =============

    conn = sqlite3.connect('cloths.db')
    
    conn.execute('''INSERT INTO REGISTRATION(Full_name,
                                      Plot_no,
                                      Street,
                                      State,
                                      City,
                                      Pincode,
                                      Email,
                                      Password,
                                      Mobile_no
                                      )VALUES(?,?,?,?,?,?,?,?,?)''',(a,b,c,d,e,f,g,h,i))
    conn.commit()
    conn.close()


'''#==== BG IMAGE ========
bg=ImageTk.PhotoImage(file="images/login.jpg")
bg_image=Label(root, image=bg)
bg_image.place(x=0,y=0,relwidth=1,relheight=1)'''

#==== registration bg =====
Frame_reg=Frame(root,bg="black")
Frame_reg.place(x=50,y=70,height=600,width=500)

#==== registration Frame =====
Frame_reg=Frame(root,bg="black")
Frame_reg.place(x=1,y=1,width=1350,height=700)


Label(root, text="CLOTHING STORE", font=("Helvetica",30,"bold"),bg="black", fg="red",bd=10).place(x=0,y=0)

Registration = Label(root, text="Registration Form", font=("Helvetica",30,"bold"),bg="black", fg="Grey",bd=10)
Registration.place(x=200,y=70)

#=== LABELS =========s

lbl_name = Label(root, text="Full Name : ", font=("Helvetica",20,"bold"),bg="black", fg="grey",bd=10)
lbl_name.place(x=50,y=140)

lbl_plot = Label(root, text=" Plot no : ", font=("Helvetica",20,"bold"),bg="black", fg="grey",bd=10)
lbl_plot.place(x=50,y=190)

lbl_street = Label(root, text=" Street : ", font=("Helvetica",20,"bold"),bg="black", fg="grey",bd=10)
lbl_street.place(x=50,y=240)

lbl_state = Label(root, text=" State : ", font=("Helvetica",20,"bold"),bg="black", fg="grey",bd=10)
lbl_state.place(x=50,y=290)

lbl_city = Label(root, text=" City : ", font=("Helvetica",20,"bold"),bg="black", fg="grey",bd=10)
lbl_city.place(x=50,y=340)

lbl_pincode = Label(root, text=" Pincode : ", font=("Helvetica",20,"bold"),bg="black", fg="grey",bd=10)
lbl_pincode.place(x=50,y=390)

lbl_email = Label(root, text=" Email : ", font=("Helvetica",20,"bold"),bg="black", fg="grey",bd=10)
lbl_email.place(x=50,y=440)

lbl_password = Label(root, text=" Password : ", font=("Helvetica",20,"bold"),bg="black", fg="grey",bd=10)
lbl_password.place(x=50,y=490)

lbl_mobile = Label(root, text=" Mobile no : ", font=("Helvetica",20,"bold"),bg="black", fg="grey",bd=10)
lbl_mobile.place(x=50,y=540)


#=== ENTRIES ================ ENTRIES ================ ENTRIES ================= ENTRIES =================

Full_name = Entry(root, font=("Helvetica",15,"bold"), fg="grey",bd=5, width=25)
Full_name.place(x=260,y=150)

Plot_no = Entry(root, font=("Helvetica",15,"bold"), fg="grey",bd=5, width=25)
Plot_no.place(x=260,y=200)

Street = Entry(root, font=("Helvetica",15,"bold"), fg="grey",bd=5, width=25)
Street.place(x=260,y=250)

State = Entry(root, font=("Helvetica",15,"bold"), fg="grey",bd=5, width=25)
State.place(x=260,y=300)

City = Entry(root, font=("Helvetica",15,"bold"), fg="grey",bd=5, width=25)
City.place(x=260,y=350)

Pincode = Entry(root, font=("Helvetica",15,"bold"), fg="grey",bd=5, width=25)
Pincode.place(x=260,y=400)

Email = Entry(root, font=("Helvetica",15,"bold"), fg="grey",bd=5, width=25)
Email.place(x=260,y=450)

Password = Entry(root, font=("Helvetica",15,"bold"), fg="grey",bd=5, width=25)
Password.place(x=260,y=500)

Mobile_no = Entry(root, font=("Helvetica",15,"bold"), fg="grey",bd=5, width=25)
Mobile_no.place(x=260,y=550)

chkbtn = Checkbutton(root,font=("Helvetica",10,"bold"), fg="grey",bg="black" ,text="        I  agree  The  Terms  &  Conditions", onvalue=1,offvalue=0)
chkbtn.place(x=150,y=600)

#==== BUTTON ========
btn_reg = Button(root, text="Register",font=("times new roman",15,"bold"),bg="black",fg="grey", width="10" ,bd=3,relief=GROOVE, command=database)
btn_reg.place(x=200,y=630)


lbl_armour = Label(root, text="Fashion  Is  The  Armor To Survive The Reality", font=("Helvetica",25,"bold"),bg="black", fg="grey",bd=10)
lbl_armour.place(x=550,y=250)


lbl_armour = Label(root, text="Of Everyday Life", font=("Helvetica",25,"bold"),bg="black", fg="grey",bd=10, width=22)
lbl_armour.place(x=650,y=305)

lbl_success = Label(root, text="If Registration is successful plez login here", font=("Helvetica",10,"bold"),bg="black", fg="grey")
lbl_success.place(x=750,y=450)

btn_login = Button(root, text="Login",font=("times new roman",15,"bold"),bg="black",fg="grey", width="10" ,bd=3,relief=GROOVE, command=login_window)
btn_login.place(x=820,y=500)


root.mainloop()