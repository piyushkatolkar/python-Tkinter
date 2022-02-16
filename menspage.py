import tkinter
from tkinter import *

a=Tk()
a.title("Mens")
a.geometry("1350x700+0+0")


def tshirts_window():
    a.destroy()
    import tshirts

#==== Login Frame 1===========
Frame_login=Frame(a,bg="black")
Frame_login.place(x=5,y=60,height=630,width=380)

#==== Login Frame 2 ==========
Frame_login=Frame(a,bg="black")
Frame_login.place(x=395,y=10,height=680,width=946)

lbl_cloth = Label(a, text="CLOTHING STORE", font=("times new roman",30,"bold"), fg="grey",bd=10)
lbl_cloth.place(x=0,y=0)

lbl_mens = Label(a, text="Men's  Fashion", font=("times new roman",30,"bold"),bg="black", fg="red",bd=10)
lbl_mens.place(x=15,y=80)

btn_clothing = Button(a, text="Clothing's", font=("times new roman",20,"bold"),bg="black", fg="grey", relief=FLAT)
btn_clothing.place(x=15,y=160)

btn_shoes = Button(a, text="Shoes", font=("times new roman",20,"bold"),bg="black", fg="grey", relief=FLAT)
btn_shoes.place(x=15,y=230)

btn_Watches = Button(a, text="Wrist Watches", font=("times new roman",20,"bold"),bg="black", fg="grey", relief=FLAT)
btn_Watches.place(x=15,y=300)

btn_Summer = Button(a, text="Summer wear", font=("times new roman",20,"bold"),bg="black", fg="grey", relief=FLAT)
btn_Summer.place(x=15,y=370)

btn_Winter = Button(a, text="Winter wear", font=("times new roman",20,"bold"),bg="black", fg="grey", relief=FLAT)
btn_Winter.place(x=15,y=440)

lbl_mcategories = Label(a, text="Men's  Categories", font=("times new roman",25,"bold"),fg="grey", bg="black",bd=10)
lbl_mcategories.place(x=420,y=20)

#==  1st line============

#==== WHITE Frame 1 =====
Frame_login=Frame(a,bg="light grey")
Frame_login.place(x=420,y=80,height=300,width=280)

Frame_login=Frame(a,bg="light grey")
Frame_login.place(x=730,y=80,height=300,width=280)

Frame_login=Frame(a,bg="light grey")
Frame_login.place(x=1040,y=80,height=300,width=280)

#==== Image 1===========
photo1 = PhotoImage(file='images\\nike.png')
label = Label(a, image=photo1)
label.place(x=430,y=90,width=260,height=240)

btn_tshirt = Button(a, text="T-Shirts", font=("times new roman",15,"bold"),fg="black", bg="light grey", relief=FLAT, command=tshirts_window)
btn_tshirt.place(x=500,y=335)

#==== Image 2===========
photo2 = PhotoImage(file='images\\shirt.png')
label = Label(a, image=photo2)
label.place(x=740,y=90,width=260,height=240)

btn_shirt = Button(a, text="Shirts", font=("times new roman",15,"bold"),fg="black", bg="light grey", relief=FLAT)
btn_shirt.place(x=830,y=335)

btn_jeans = Button(a, text="Jeans", font=("times new roman",15,"bold"),fg="black", bg="light grey", relief=FLAT)
btn_jeans.place(x=1150,y=335)

#============ 2nd line =============== 2nd line =================== 2nd line ==================== 2nd line

#==== WHITE Frame =================
Frame_login=Frame(a,bg="light grey")
Frame_login.place(x=420,y=387,height=300,width=280)

Frame_login=Frame(a,bg="light grey")
Frame_login.place(x=730,y=387,height=300,width=280)

btn_trawser = Button(a, text="Torwser's", font=("times new roman",15,"bold"),fg="black", bg="light grey", relief=FLAT)
btn_trawser.place(x=490,y=640)

btn_Inner = Button(a, text="Inner wear", font=("times new roman",15,"bold"),fg="black", bg="light grey", relief=FLAT)
btn_Inner.place(x=810,y=640)


a.mainloop()