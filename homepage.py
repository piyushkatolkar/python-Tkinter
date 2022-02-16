import tkinter
from tkinter import *
from PIL import ImageTk


root=Tk()
root.title("Home")
root.geometry("1350x700+0+0")

def mens_window():
    root.destroy()
    import menspage


#==== HEADER CODE =====
#==== BLACK Frame =====
Frame_login=Frame(root,bg="black")
Frame_login.place(x=0,y=0,height=694,width=1400)

#==== Image ===========
photo = PhotoImage(file='images\\home.png')
label = Label(root, image=photo)
label.place(x=10,y=131,width=1330,height=200)


#==== BODY ==================== BODY ====================== BODY ===================== BODY =================

Label(root, text="CLOTHING STORE", font=("Helvetica",30,"bold"), bg="black", fg="grey",bd=10).place(x=0,y=0)

btn_login = Button(root, text="Login", font=("Helvetica",15,"bold"),bg="black",fg="grey", relief=FLAT)
btn_login.place(x=0,y=70)

lbl_prime = Label(root, text="or", font=("Helvetica",15,"bold"), bg="black", fg="grey")
lbl_prime.place(x=80,y=74)

btn_signup = Button(root, text="Signup", font=("Helvetica",15,"bold"),bg="black",fg="grey", relief=FLAT)
btn_signup.place(x=120,y=70)

searchbox=Entry(root, font=("Helvetica",20,"bold"),bg="grey",fg="black",width="35",bd=5)
searchbox.place(x=400,y=10)

search = Button(root, text="Search",font=("Helvetica",14,"bold"),bg="black",fg="grey",bd=5,relief=GROOVE)
search.place(x=970,y=10)

account = Button(root, text="Account settings", font=("Helvetica",15,"bold"),bg="black",fg="grey", relief=FLAT)
account.place(x=1070,y=10)

cart = Button(root, text="cart", font=("Helvetica",15,"bold"),bg="black",fg="grey",width="5", relief=FLAT)
cart.place(x=1260,y=10)

mens = Button(root, text="Mens",font=("Helvetica",15,"bold"),bg="black",fg="grey",width="15",bd=5,relief=FLAT, command=mens_window)
mens.place(x=200,y=70)

womens = Button(root, text="Womens",font=("Helvetica",15,"bold"),bg="black",fg="grey",bd=5,width="15",relief=FLAT)
womens.place(x=397,y=70)

kids = Button(root, text="Kids",font=("Helvetica",15,"bold"),bg="black",fg="grey",bd=5,width="15",relief=FLAT)
kids.place(x=594,y=70)

home = Button(root, text="Home living",font=("Helvetica",15,"bold"),bg="black",fg="grey",bd=5,width="15",relief=FLAT)
home.place(x=791,y=70)

essentials = Button(root, text="Essentials",font=("Helvetica",15,"bold"),bg="black",fg="grey",bd=5,width="15",relief=FLAT)
essentials.place(x=988,y=70)

#==== Image ===========
photo = PhotoImage(file='images\\home.png')
label = Label(root, image=photo)
label.place(x=10,y=131,width=1330,height=200)


#==== BODY IMAGES =======

#==== WHITE Frame 1 =====
Frame_login=Frame(root,bg="light grey")
Frame_login.place(x=10,y=340,height=350,width=320)
#==== Image WEB 1===========
photo1 = PhotoImage(file='images\\web.png')
label = Label(root, image=photo1)
label.place(x=30,y=400)

lbl_hi = Label(root, text="Hi, Piyush", font=("times new roman",20,"bold"), bg="light grey", fg="black")
lbl_hi.place(x=100,y=340)
top_links = Label(root, text="Top links for you", bg="light grey", fg="black")
top_links.place(x=28,y=375)

#==== WHITE Frame 2=====
Frame_login=Frame(root,bg="light grey")
Frame_login.place(x=347,y=340,height=350,width=320)
#==== Image WEB 2 ===========
photo2 = PhotoImage(file='images\\payments.png')
label = Label(root, image=photo2)
label.place(x=367,y=400,height=270)

Donations = Label(root, text="Donations,  recharges,  bills,", font=("times new roman",15,"bold"), bg="light grey", fg="black")
Donations.place(x=369,y=340)
med_mors = Label(root, text="medicines  &  more", font=("times new roman",15,"bold"), bg="light grey", fg="black")
med_mors.place(x=369,y=366)

#==== WHITE Frame 3 =====
Frame_login=Frame(root,bg="light grey")
Frame_login.place(x=684,y=340,height=350,width=320)
#==== Image WEB3 ===========
photo3 = PhotoImage(file='images\\movies.png')
label = Label(root, image=photo3)
label.place(x=704,y=400,height=270)

lbl_prime = Label(root, text="Prime Movies", font=("times new roman",20,"bold"), bg="light grey", fg="black")
lbl_prime.place(x=704,y=340)

#==== WHITE Frame 4 =====
Frame_login=Frame(root,bg="light grey")
Frame_login.place(x=1020,y=340,height=350,width=320)
#==== Image WEB 4 ===========
photo4 = PhotoImage(file='images\\cycle.png')
label = Label(root, image=photo4)
label.place(x=1040,y=400,height=270)

lbl_deals = Label(root, text="Deals & Promotions", font=("times new roman",20,"bold"), bg="light grey", fg="black")
lbl_deals.place(x=1040,y=340)
 

root.mainloop()
