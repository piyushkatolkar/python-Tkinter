import tkinter
from tkinter import *

a=Tk()
a.title("T-Shirt Info")
a.geometry("1350x700+0+0")

def payment_window():
    a.destroy()
    import payment

#===== main background color =====================================================================

Frame_login=Frame(a, bg="grey")
Frame_login.place(x=0, y=0, width=1350, height=700)

lbl_cloth = Label(a, text="CLOTHING STORE", font=("Helvetica",30,"bold"),bg="grey", fg="red",bd=10)
lbl_cloth.place(x=0,y=0)

Frame_login=Frame(a, bg="black")
Frame_login.place(x=10,y=100,height=500,width=400)

lbl_grey = Label(a, text="Mens Grey T-Shirt",font=("Helvetica",20,"bold"), bg="grey" ,fg="black",bd=10)
lbl_grey.place(x=600,y=100)

lbl_price = Label(a, text="Price : INR 499 + free shipping & Import Fees",font=("Helvetica",15), bg="grey" ,fg="black")
lbl_price.place(x=600,y=170)

lbl_fit = Label(a, text="Fit : True to size",font=("Helvetica",15), bg="grey" ,fg="black")
lbl_fit.place(x=600,y=200)

btn_buy = Button(a, text="Buy Now", font=("Helvetica",15,"bold"),fg="grey", bg="black", relief=FLAT, command=payment_window)
btn_buy.place(x=600,y=250)

lbl_fit = Label(a, text="-  100% cotton",font=("Helvetica",15), bg="grey" ,fg="black")
lbl_fit.place(x=600,y=350)

lbl_fit = Label(a, text="-  Imported",font=("Helvetica",15), bg="grey" ,fg="black")
lbl_fit.place(x=600,y=380)

lbl_fit = Label(a, text="-  Machine Wash",font=("Helvetica",15), bg="grey" ,fg="black")
lbl_fit.place(x=600,y=410)

lbl_fit = Label(a, text="-  Same fit, new name: We,ve changed the name of this shirt style to loose fit but the measurements remains the same",font=("Helvetica",15), bg="grey" ,fg="black")
lbl_fit.place(x=600,y=440)

lbl_fit = Label(a, text="-  Model is 6'1 and wearing size medium ",font=("Helvetica",15), bg="grey" ,fg="black")
lbl_fit.place(x=600,y=470)

lbl_fit = Label(a, text="-  Fit : True to size",font=("Helvetica",15), bg="grey" ,fg="black")
lbl_fit.place(x=600,y=500)

a.mainloop()
