import tkinter
from tkinter import *

a=Tk()
a.title("T-Shirts")
a.geometry("1350x700+0+0")

def grey_window():
    a.destroy()
    import tshirtinfo

#==== Login Frame 1===========
Frame_login=Frame(a,bg="black")
Frame_login.place(x=5,y=60,height=630,width=380)


#==== WHITE Frame 1 =====
Frame_login=Frame(a,bg="light grey")
Frame_login.place(x=420,y=80,height=300,width=280)

Frame_login=Frame(a,bg="light grey")
Frame_login.place(x=730,y=80,height=300,width=280)

Frame_login=Frame(a,bg="light grey")
Frame_login.place(x=1040,y=80,height=300,width=280)

'''#==== Image WEB 1===========
photo1 = PhotoImage(file='images\\tshirt.png')
label = Label(a, image=photo1)
label.place(x=30,y=400,width=300,height=200)'''

lbl_cloth = Label(a, text="CLOTHING STORE", font=("times new roman",30,"bold"), fg="grey",bd=10)
lbl_cloth.place(x=0,y=0)

btn_tshirt = Button(a, text="Mens Grey T-Shirt", font=("times new roman",15,"bold"),fg="black", bg="light grey", relief=FLAT, command=grey_window)
btn_tshirt.place(x=480,y=335)

btn_shirt = Button(a, text="mens white tshirts", font=("times new roman",15,"bold"),fg="black", bg="light grey", relief=FLAT)
btn_shirt.place(x=800,y=335)

btn_jeans = Button(a, text="mens red tshirt", font=("times new roman",15,"bold"),fg="black", bg="light grey", relief=FLAT)
btn_jeans.place(x=1100,y=335)

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